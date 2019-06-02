#!/usr/bin/perl

##############################
## pragmas & encoding setup

use strict;
use warnings;

use utf8; # Process strings within this script as utf-8
binmode(STDOUT, ":utf8"); # write to STDOUT as utf-8

##############################
## Glossary

# Our input file needs to exist or no point in running this script
my $ifd; # aka input file descriptor
open($ifd, "< my-clippings.txt") or die "Error: couldn't open my-clippings.txt. $!\n";

my $outfolder = "highlights"; # folder where our index and book-specific files live

my $ofile; # book file we're writing to at the moment
my $ofd; # output file descriptor

my $tempfile; # backup copy of book file, used while writing
my $tempfd; # temp file descriptor

my $kbinput; # temp storage for data from keyboard
my $kb; # keyboard file descriptor

my $indexfile = "$outfolder/.index.txt"; # index filename
my $indexfd; # index file descriptor

my %tr; # index TRanslator

# temp storage
my ($rawtitle, $title, $author, $key, $type, $loc, $content) = '';
my $state;


##############################
## loadIndex: parse .index.txt to generate %tr
## %tr has a list of keys which are each a raw title
## each key maps to a cleaner/simplified title and author

sub loadIndex {

  my %output = (); # translation hash
  my @index; # temp storage for index data
  my $state = 1; # 0-raw, 1-title, 2-authors, 3-restart & raw
  my ($rawtitle, $title, $author) = '';

  # Create an empty index file if one doesn't already exist
  unless ( -e $indexfile) {
    open($indexfd, "> $indexfile") or die "Error: couldn't open $indexfile. $!\n";
    print $indexfd "\n";
    close($indexfd) or die "Error: couldn't close '$indexfile' $!\n";
  }

  # Load the raw index file into memory
  open($indexfd, "< $indexfile") or die "Error: couldn't open '$indexfile' $!\n";
  @index = <$indexfd>;
  close($indexfd) or die "Error: couldn't close '$indexfile' $!\n";

  # Parse the raw index file into a perl hash table
  foreach (@index) {

    s/[\s]*$//g; # remove trailing whitespace
    s/^[\xef\xbb\xbf]*//g; # remove leading BOM
  
    if ($_ eq '') { next; }                 # skip empty rows
    elsif ($state == 1) { $rawtitle = $_; } # first line is the raw title aka hash key
    elsif ($state == 2) { $title = $_; }    # second line is the clean title
    elsif ($state == 3) { $author = $_;     # third line is the clean author

      # at the third line, it's time to save the data we've gathered
      $output{$rawtitle} = {title => $title, author => $author};
      # and reset in preparation for the next index entry
      $rawtitle = ""; $title = "", $author = ""; $state = 0;
    }
    $state += 1;
  }
  return %output;
}
%tr = loadIndex();

# # debug index: print all %tr keys and values
# foreach (sort keys %tr) {
#   print "'$_' : '$tr{$_}->{'title'}' by '$tr{$_}->{'author'}'\n";
# }
# exit;

##############################
## Read My Clippings (from stdin or as 1st arg)

# reset temp storage
($rawtitle, $title, $author, $key, $type, $loc, $content, $loc) = '';
$state = 1; # state: 1-title/author, 2-type/location/date, 3-highlight/note

while ($_ = <$ifd>) {

  ##############################
  ## line cleanup

  s/[\s]*$//g; # remove trailing whitespace
  s/^[\xef\xbb\xbf]*//g; # remove leading BOM

  if ($_ eq '') { next; } # ignore empty lines

  ##############################
  ## Divider Line: Write out our current data and reset variables

  if ($_ eq "==========") { 

    $ofile = "$outfolder/" . lc "$title.md";
    $ofile =~ s/\s/-/g;

    # print "GOT\ntitle: $title\nauthor: $author\ntype: $type\nloc: $loc\ncontent: $content\n\n";

    ##############################
    ## Add this content to an existing file
  
    if ($type eq "Bookmark") {} # BTW skip bookmarks
    elsif ( -e $ofile) {

      $tempfile = "$ofile.tmp";
      my $templine = "";
      my $isDupe = 0;

      # Open $ofile and a temporary file to copy to
      open($ofd, "< $ofile") or die "Error: couldn't open $ofile. $!\n";
      open($tempfd, "> $tempfile") or die "Error: couldn't open $tempfile. $!\n";

      ##############################
      ## Copy over the first half of outfile, 
      ## Stop when we find a good spot to insert our new content
      while (<$ofd>) {
        if (/\s((?:pg)|(?:loc))\s(\d+)\s-\s(.*)/) {
          if ($2 == $loc && ( $3 eq $content || $3 eq "My Note: $content") ) {
            # print "duplicate detected!\n";
            $isDupe = 1;
            last; # abort
          } elsif ($2 <= $loc) {
            print $tempfd $_;
            # print "new info at $loc comes after $2\n";
          } else {
            # print "new info at $loc goes here: $2\n";
            $templine = $_;
            last;
          }
        } else {
          print $tempfd $_;
        }
      }

      ##############################
      ## Add this line of content
      if ($type eq "Highlight") { print $tempfd " - loc $loc - $content\n"; }
      elsif ($type eq "Note") { print $tempfd " - loc $loc - My Note: $content\n"; }

      # if this is a duplicate we just added a copy above
      print $tempfd "\n$templine" unless($isDupe);
    
      ##############################
      # copy over the rest of the current file & cleanup
      while (<$ofd>) { print $tempfd $_; }  

      close($tempfd) or die "Error: couldn't close $tempfile. $!\n";
      close($ofd) or die "Error: couldn't close $ofile. $!\n";

      # replace our old outfile with our new one
      unlink $ofile;
      rename $tempfile, $ofile;

    ##############################
    ## Create a new file and initialize it with this content

    } else {
      # initialize a file for this new book
      open($ofd, "> $ofile") or die "Error: couldn't open $ofile. $!\n";

      # Add the title & author to the file header
      print $ofd "\n#  $title\n";
      print $ofd "\n## by $author\n\n";

      # Add this file's first piece of content
      print $ofd " - loc $loc - $content\n\n";
      close($ofd) or die "Error: couldn't close $ofile. $!\n";
    }

    ##############################
    ## Reset in preparation for the next piece of content

    ($rawtitle, $title, $author, $key, $type, $loc, $content) = "";
    $state = 1; 
  }

  ##############################
  ## 1st Line: Title & Author
  elsif ($state == 1) {

    # extract the title and maybe the author
    if (/^(.*)\((.*)\)\s*$/) { 
      $key = $1; $author = $2;
      $key =~ s/[\s]*$//;
    } else {
      $key = $_; $author = "";
    }

    ##############################
    ## Old book? Replace extracted title/author w data from Index
    if (exists $tr{$key}) {
      $author = $tr{$key}->{'author'};
      $title = $tr{$key}->{'title'};
      # print "Fetched from index: '$title' by '$author'\n";
    }

    ##############################
    ## New book? Add a new entry to our index
    else {

      print "New book: '$key' by '$author'\n";
      open($kb, "< /dev/tty") or die "Error: couldn't open keyboard. $!\n";

      # Ask the user what the TITLE of this book should be displayed as
      print "Display title: "; chomp($kbinput = <$kb>); # chomp = s/\n?$//
      # set title to input unless the input is empty (in which case use default)
      if ($kbinput ne '') { $title = $kbinput; }
      else { $title = $key; }

      # Ask the user what the AUTHOR of this book should be displayed as
      print "Display author: "; chomp($kbinput = <$kb>); # chomp = s/\n?$//
      # set author to input unless the input is empty (in which case use default)
      if ($kbinput ne '') { $author = $kbinput; }

      close($kb) or die "Error: couldn't close keyboard. $!\n";

      # Save this info to our index
      open($indexfd, ">> $indexfile") or die "Error: couldn't open '$indexfile' $!\n";
      print $indexfd "\n$key\n$title\n$author\n";
      close($indexfd) or die "Error: couldn't close '$indexfile' $!\n";

      %tr = loadIndex();

    }
    $state += 1;
  }

  ##############################
  ## 2nd Line: Type & Location & Date
  elsif ($state == 2) {

    # Get Type
    if (/^-\sYour\s((?:Highlight)|(?:Note)|(?:Bookmark))/) {
      $type = $1; # print "type: $type\n";
    } else {
      die "Error: could not get type for: '$_'\n";
    }  

    # Get Location
    if (/Location\s([\d]+)/) {
      $loc = $1; # print "location: $loc\n";
    } elsif (/[Pp]age\s([\d]+)/) {
      $loc = $1; # print "page: $loc\n";
    } else {
      die "Error: could not get location for: '$_'\n";
    }

    $state += 1;
  }

  ##############################
  ## 3rd line: Note/Highlight Content
  elsif ($state == 3) { $content = $_; }

  ##############################
  ## More than 3 lines or less than 1: something's wrong
  else { die "Error: invalid state: $state on line '$_'\n"; }

}

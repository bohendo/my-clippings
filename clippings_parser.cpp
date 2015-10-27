#include <iostream> //std::cout, std::cin
#include <string>   //std::string
#include <fstream>  //
#include <vector>

// This function will accept the 6-8 lines that make up one highlight or note
// This function will return the string that should be added to the outfile
void parse_chunk(std::vector<std::string> line[]);

int main() {

  // Instead of user input, this should accept a command line argument.
  std::cout << "Enter Kindle file to parse: ";
  std::string input_filename;
  std::getline(std::cin, input_filename);

  // If there is no user input, use default clippings filename
  if (input_filename == "") {
    input_filename = "My Clippings.txt";
  }

  // Print a message that tells the user "I'm working on it"
  std::cout << "Parsing " << input_filename << "..." << std::endl;

  // access the file to parse
  std::ifstream my_clippings (input_filename);
  if (my_clippings.good()) {
    std::cout << "File access granted!" << std::endl;
  }
  else {
    std::cout << "File access failed!" << std::endl;
  }

  // define some variables that we'll use to store info
  std::string line;
  std::string currbook;
  int currchunk = 1;
  int currpage;
  int i = 1;
  std::vector<std::string> chunk;

  // until we get to the end of the infile...
  while (std::getline(my_clippings, line)) {

    // end the current chunk when we encounter this line
    if (line != "==========") {
      parse_chunk(chunk);
      i = 0;
    }
    // Otherwise, the chunk continues to grow...?
    else {
      // currently have some kind of segmentation fault... no idea why
      chunk[i++] = line;
    }
  }

  
  my_clippings.close();
  //output.close();
  system("PAUSE");
  return 0;
}


void parse_chunk(std::vector<std::string> chunk_input){
  
  int i = 1;
  std::cout << "chunk number " << i++ << std::endl;
  
}

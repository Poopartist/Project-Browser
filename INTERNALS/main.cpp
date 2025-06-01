#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <filesystem>
#include <algorithm>

namespace fs = std::filesystem;

void searchFiles(const std::string& dir, const std::string& query) {
    std::vector<std::string> found;
    for (const auto& entry : fs::directory_iterator(dir)) {
        std::ifstream file(entry.path());
        std::string line, content;
        while (std::getline(file, line)) content += line + " ";
        if (content.find(query) != std::string::npos)
            found.push_back(entry.path().filename().string());
    }
    if (found.empty())
        std::cout << "No results found.\n";
    else
        for (const auto& f : found)
            std::cout << "Found in: " << f << "\n";
}

void createWebsite(const std::string& dir) {
    std::string title, content;
    std::cout << "Title: ";
    std::getline(std::cin, title);
    std::cout << "HTML Content:\n";
    std::getline(std::cin, content);
    std::string fname = dir + "/" + title + ".html";
    std::ofstream file(fname);
    file << "<h1>" << title << "</h1>\n" << content;
    std::cout << "Website created: " << fname << "\n";
}

int main() {
    const std::string dir = "websites";
    fs::create_directory(dir);
    while (true) {
        std::cout << "1. Search Websites\n2. Create Website\n3. Exit\nChoice: ";
        int choice;
        std::cin >> choice;
        std::cin.ignore();
        if (choice == 1) {
            std::string q;
            std::cout << "Enter search query: ";
            std::getline(std::cin, q);
            searchFiles(dir, q);
        } else if (choice == 2) {
            createWebsite(dir);
        } else {
            break;
        }
    }
    return 0;
}
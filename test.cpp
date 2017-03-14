#include <string>
#include <vector>

struct Foo {
  int bar[];
};

int main(int argc, char const* argv[]) {
  std::vector<std::string> vec;
  vec.push_back("hello");
  for (const auto& s : vec) {
    s.c_str();
  }
  Foo f;
}
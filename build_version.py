class InvalidBuild(ValueError):
    pass


class  BuildVersion:
    """
    This class is a custom Data type for Build 
    and to compare build for equality and in-equality
    such as 
        < (less than) 
        > (greater than) 
        == (equals to)
    
    parameters:
        build (str): Build number in string format E.g. 202007.12
    
    example:
        BuildVersion(202007.6) < BuildVersion(202007.12)   # This returns True
        BuildVersion(202007.8) > BuildVersion(202007.7)    # This returns True
        BuildVersion(202007.12) == BuildVersion(202007.12) # This returns True
    """
    def __init__(self, build):
        if '.' not in build:
            raise InvalidBuild("The Build is not valid")
        self.build = build
        
    @property
    def build_number(self):
        return int(self.build.split(".")[0])
    
    @property
    def patch_number(self):
        return int(self.build.split(".")[1])
    
    @property
    def build_length(self):
        return len(self.build.split('.'))
    
    def __str__(self):
        return f"{self.build}"
    
    def __lt__(self, another_build):
        """ Comparision between Build for less-than operation """
        if self.build_length == another_build.build_length:
            if (self.build_number <= another_build.build_number) \
                and (self.patch_number < another_build.patch_number):
                return True
            else:
                return False
        else:
            return f"Build Mismatch between {self} and {another_build}"
        
    def __gt__(self, another_build):
        """ Comparision between Build for greater-than operation """
        if self.build_length == another_build.build_length:
            if (self.build_number >= another_build.build_number) \
                and (self.patch_number > another_build.patch_number):
                return True
            else:
                return False
        else:
            return f"Build Mismatch between {self} and {another_build}"
        
    def __eq__(self, another_build):
        """ Comparision between Build for equality operation """
        if self.build_length == another_build.build_length:
            if (self.build_number == another_build.build_number) \
                and (self.patch_number == another_build.patch_number):
                return True
            else:
                return False
        else:
            return f"Build Mismatch between {self} and {another_build}"
    
if __name__ == "__main__":
    build_version = BuildVersion("202007.6")
    another_build = BuildVersion("202007.12")
    print(build_version > another_build)
    print(build_version < another_build)
    print(build_version == another_build)

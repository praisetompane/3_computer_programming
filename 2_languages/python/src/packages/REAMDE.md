def: module: a collection of code 
            1 type of module object
            all modules are of this type
            independent of technolgy(e..g python, C, etc)

            has: 
                name

def: package: special kind of module for orgnising other modules
                has: 
                    __path__ attribute 

                provide:
                    naming hierarchy

                    metaphor: package := directories on a file system, then
                            module  := files in the directories
                            
                sub modules access nootation
                    parent.child.child...
                    e.g. email.mime.text
                
                types:
                    regular package:
                        has:
                            __init__.py file
                                NB: executed on package import
                                decorated at import time with additional attributes

                            e.g.
                                email
                                    __init__.py
                                    text
                                        __init__.py
                                    html
                                        __init__.py
                                    binary
                                        __init__.py
                                    sender.py

                            NB: importing email.text
                                    executes email.__init__.py AND text.__init__.py
                                    subsequent imports of html or binary
                                        only their __init__.py is executed
                                
                    namespace package:
                        def:    composite of various portions
                                    each portiion constributes a subpackage
                                        to the parent package.
                        properties:
                            portions can exist anywhere Python searhces during module import
                            they may/may not correspond directly to objects on a file sytem;
                            can be virtual modules with no concrete representation.
                            __path__ : custom iterable type
                            parent/__init__.py is NOT required
                                there may be multiple "parent" directories
                                    in different locations
                                    e.g.
                                        parent/one
                                        parent/three
                        



            

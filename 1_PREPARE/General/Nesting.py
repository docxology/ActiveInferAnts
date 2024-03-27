import json
from typing import Dict, Any, Union

class CategoryTheorySystem:
    """
    A class to represent and manipulate systems based on Category Theory concepts,
    allowing for the arbitrary nesting of systems. It supports adding objects, morphisms,
    and nested systems, along with serialization and deserialization of the system state.
    """
    
    def __init__(self):
        self.system_components = {
            "objects": {},
            "morphisms": {},
            "systems": {}
        }
    
    def add_component(self, component_type: str, name: str, *args, **kwargs) -> None:
        """
        General method to add objects, morphisms, or systems.
        """
        if component_type == "object":
            self.system_components["objects"][name] = kwargs
        elif component_type == "morphism":
            self.system_components["morphisms"][name] = {
                "source": args[0], "target": args[1], **kwargs
            }
        elif component_type == "system":
            self.system_components["systems"][name] = {
                "objects": args[0], "morphisms": args[1]
            }
        else:
            raise ValueError(f"Unknown component type: {component_type}")
    
    def serialize_system(self, filename: str) -> None:
        """
        Serialize the system to a JSON file.
        """
        with open(filename, 'w') as file:
            json.dump(self.system_components, file, indent=4)
    
    def load_system(self, filename: str) -> None:
        """
        Load a system from a JSON file.
        """
        with open(filename, 'r') as file:
            self.system_components = json.load(file)

# Example usage
if __name__ == "__main__":
    ct_system = CategoryTheorySystem()
    ct_system.add_component("object", "ObjectA", property1="value1")
    ct_system.add_component("object", "ObjectB", property2="value2")
    ct_system.add_component("morphism", "Morphism1", "ObjectA", "ObjectB", propertyM="valueM")
    ct_system.add_component("system", "NestedSystem1", {"ObjectA": {"property1": "value1"}}, {"Morphism1": {"source": "ObjectA", "target": "ObjectB", "propertyM": "valueM"}})
    ct_system.serialize_system("category_theory_system.json")

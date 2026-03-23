import os
import re

class BitPoetKeywordSizeNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompt": ("STRING", {"default": ""}),
                "size_definitions": ("STRING", {
                    "multiline": True,
                    "default": "[default]:1024x1024",
                    "placeholder": "Enter your size definitions line by line ([keyword]:WxH)..."
                }),
                "remove_if_found": ("BOOLEAN", {"default": True})
            }
        }
    
    RETURN_TYPES = ("STRING", "INT", "INT", )
    RETURN_NAMES = ("prompt", "width", "height", )

    FUNCTION = "keyword_size"
    CATEGORY = "bitpoet/utils"
    
    SEARCH_ALIASES = ["keyword size", "keyword sizer", "size by keyword"]

    def keyword_size(self, prompt, size_definitions, remove_if_found):

        default_w = 1024
        default_h = 1024

        for line in size_definitions.splitlines():
            if line.startswith("#"):
                continue
            (keyword, sizedef) = line.split(":")
            if keyword == "[default]":
                (default_w, default_h) = sizedef.split("x")
            if keyword in prompt:
                (w, h) = sizedef.split("x")
                if remove_if_found:
                    prompt_out = prompt.replace(keyword, "")
                    return (prompt_out, w, h, )
        
        return (prompt, default_w, default_h, )
            
    


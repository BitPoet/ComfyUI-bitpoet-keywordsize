# ComfyUI-bitpoet-keywordsize
Simple ComfyUI node that determines the image size by a keyword in the prompt, optionally replacing the keyword

## Usage

Add the node to your workflow.   
Connect your prompt to the prompt input.   
Input an arbitrary number of definitions in the form [keyword]:WIDTHxHEIGHT, one per line.   
Connect the outputs prompt, width and height.   
Optionally, toggle the remove_if_found switch, which will strip the found keyword from the prompt.   

Aside from the [default] keyword, you can format your keywords however you like.

## License

Released under GNU Public License V3. See file "LICENSE" for details.

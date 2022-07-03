#!/bin/bash

# TODO: Scan the ./inputs subdirectory (which contains .mmd files), then generate a new ./outputs subdirectory (containing .png or .svg files) using the mermaid-js-cli. 

input_name=${1:-flow_chart.mmd}
output_name=${2:-flow_chart.png}

# TODO: delete any existing file on disk already matching the output_name

# generate a new file on disk with name output_name
# this command is from `github.com/mermaid-js/mermaid-cli` docs
mmdc_command="mmdc -i ${input_name} -o ${output_name} -t dark -b transparent"
mmdc_command_result=$(${mmdc_command})

# TODO: verify that the output_name was actually produced

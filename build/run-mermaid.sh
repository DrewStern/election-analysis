#!/bin/bash

# TODO: Scan the ./inputs subdirectory (which contains .mmd files), then generate a new ./outputs subdirectory (containing .png or .svg files) using the mermaid-js-cli. 

input_name=${1:-flow_chart.mmd}
output_name=${2:-flow_chart.png}

arch_input_path="../docs/arch/input"
full_input_path=${arch_input_path}/${input_name}

arch_output_path="../docs/arch/output"
full_output_path=${arch_output_path}/${output_name}

# TODO: delete any existing file on disk already matching the output_name
# cd ../docs/arch/output

# generate a new file on disk with name output_name
# this command is from `github.com/mermaid-js/mermaid-cli` docs
mmdc_command="mmdc -i ${full_input_path} -o ${full_output_path} -t dark -b transparent"
mmdc_command_result=$(${mmdc_command})

# TODO: verify that the output_name was actually produced

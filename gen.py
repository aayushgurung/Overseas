# Define the spacing variables
spacing_values = {
    "4": "4px",
    "8": "8px",
    "12": "12px",
    "16": "16px",
    "24": "24px",
    "32": "32px",
    "48": "48px",
    "64": "64px",
    "96": "96px",
}

# Define breakpoints for mobile, tablet, desktop, sm, md, lg, xl
breakpoints = {
    "sm": "min-width: 640px and max-width: 767px",  # Small screens (sm)
    "md": "min-width: 768px and max-width: 1023px",  # Medium screens (md)
    "lg": "min-width: 1024px and max-width: 1279px",  # Large screens (lg)
    "xl": "min-width: 1280px",  # Extra large screens (xl)
}

# Create the utility classes
css_content = ""

# For each breakpoint, generate margin and padding utility classes
for breakpoint, query in breakpoints.items():
    for spacing, spacing_value in spacing_values.items():
        # Margin utilities
        css_content += f"@media ({query}) {{\n"
        css_content += f"  .m-{breakpoint}-{spacing} {{ margin: {spacing_value}; }}\n"
        css_content += f"  .mt-{breakpoint}-{spacing} {{ margin-top: {spacing_value}; }}\n"
        css_content += f"  .mb-{breakpoint}-{spacing} {{ margin-bottom: {spacing_value}; }}\n"
        css_content += f"  .ml-{breakpoint}-{spacing} {{ margin-left: {spacing_value}; }}\n"
        css_content += f"  .mr-{breakpoint}-{spacing} {{ margin-right: {spacing_value}; }}\n"
        css_content += f"  .mx-{breakpoint}-{spacing} {{ margin-left: {spacing_value}; margin-right: {spacing_value}; }}\n"
        css_content += f"  .my-{breakpoint}-{spacing} {{ margin-top: {spacing_value}; margin-bottom: {spacing_value}; }}\n"

        # Padding utilities
        css_content += f"  .p-{breakpoint}-{spacing} {{ padding: {spacing_value}; }}\n"
        css_content += f"  .pt-{breakpoint}-{spacing} {{ padding-top: {spacing_value}; }}\n"
        css_content += f"  .pb-{breakpoint}-{spacing} {{ padding-bottom: {spacing_value}; }}\n"
        css_content += f"  .pl-{breakpoint}-{spacing} {{ padding-left: {spacing_value}; }}\n"
        css_content += f"  .pr-{breakpoint}-{spacing} {{ padding-right: {spacing_value}; }}\n"
        css_content += f"  .px-{breakpoint}-{spacing} {{ padding-left: {spacing_value}; padding-right: {spacing_value}; }}\n"
        css_content += f"  .py-{breakpoint}-{spacing} {{ padding-top: {spacing_value}; padding-bottom: {spacing_value}; }}\n"
        css_content += "}\n"

# Save the content to a CSS file
css_file_path = "C:/Org Prj/gen.css"
with open(css_file_path, "w") as file:
    file.write(css_content)

css_file_path

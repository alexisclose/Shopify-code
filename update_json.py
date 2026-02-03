import json

file_path = r"c:\Users\nicolas\Documents\Shopify-code\Shopify-code\templates\index.json"

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# New block order: move custom_liquid_C9byWQ right before buy_buttons
new_order = [
    "title",
    "judge_me_reviews_preview_badge_rMk6ri",
    "price",
    "custom_liquid_ggN4pw",
    "variant_picker",
    "custom_liquid_C9byWQ",  # Features - moved here (before buy_buttons)
    "buy_buttons",
    "custom_liquid_9yGaAT",
    "custom_liquid_zCmbKz",
    "collapsible_tab_GLJYqE",
    "collapsible_tab_cMNkXd",
    "custom_liquid_kHkkHE",
    "text_VdDg7K"
]

data['sections']['featured_product_xyk8kz']['block_order'] = new_order

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✅ Moved features block to appear right before Add to Cart!")

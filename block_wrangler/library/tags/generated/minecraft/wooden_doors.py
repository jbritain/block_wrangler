from block_wrangler.tag import TagLibrary
from block_wrangler.library.factories import block_types


def load_tags(library:TagLibrary):
	tag = library.touch('minecraft:wooden_doors')
	
	tag.add(block_types(
		'minecraft:acacia_door',
		'minecraft:bamboo_door',
		'minecraft:birch_door',
		'minecraft:cherry_door',
		'minecraft:crimson_door',
		'minecraft:dark_oak_door',
		'minecraft:jungle_door',
		'minecraft:mangrove_door',
		'minecraft:oak_door',
		'minecraft:pale_oak_door',
		'minecraft:spruce_door',
		'minecraft:warped_door',
	strict=False))
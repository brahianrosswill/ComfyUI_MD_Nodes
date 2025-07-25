# C:\Stable Diffusion\ComfyUI\custom_nodes\ComfyUI_MD_Nodes\__init__.py

# Initialize empty dictionaries to collect all mappings
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}

# --- DIAGNOSTIC PRINTS (Keep these for now to confirm behavior) ---
#import sys
#print(f"\n--- MD_Nodes __init__.py Diagnostics ---")
#print(f"__name__: {__name__}")
#print(f"__package__: {__package__}")
#print(f"sys.path (relevant part for MD_Nodes):")
#for p in sys.path:
#    if "ComfyUI" in p and "MD_Nodes" not in p:
#        print(f"  - {p}")
#print(f"--- End MD_Nodes __init__.py Diagnostics ---\n")
# --- END DIAGNOSTIC PRINTS ---


# --- Import and add mappings from node files ---
# Using relative imports since this __init__.py is now at the package root.
try:
    from .APG_Guider_Forked import NODE_CLASS_MAPPINGS as APG_CLASS_MAPPINGS
    from .APG_Guider_Forked import NODE_DISPLAY_NAME_MAPPINGS as APG_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(APG_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(APG_DISPLAY_MAPPINGS)
except Exception as e:
    print(f"WARNING: Could not load APG_Guider_Forked: {e}")

try:
    from .NoiseDecayScheduler_Custom import NODE_CLASS_MAPPINGS as ND_CLASS_MAPPINGS
    from .NoiseDecayScheduler_Custom import NODE_DISPLAY_NAME_MAPPINGS as ND_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(ND_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(ND_DISPLAY_MAPPINGS)
except Exception as e:
    print(f"WARNING: Could not load NoiseDecayScheduler_Custom: {e}")

# --- Import the ORIGINAL PingPong Sampler Custom ---
try:
    from .PingPongSampler_Custom import NODE_CLASS_MAPPINGS as PPS_CLASS_MAPPINGS
    from .PingPongSampler_Custom import NODE_DISPLAY_NAME_MAPPINGS as PPS_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(PPS_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(PPS_DISPLAY_MAPPINGS)
    print("INFO: Successfully loaded original PingPong Sampler (Custom).")
except Exception as e:
    print(f"WARNING: Could not load PingPongSampler_Custom: {e}")

# --- Import the FBG-integrated PingPong Sampler (V0.9.9) ---
try:
    from .PingPongSampler_Custom_FBG import NODE_CLASS_MAPPINGS as PPS_FBG_CLASS_MAPPINGS
    from .PingPongSampler_Custom_FBG import NODE_DISPLAY_NAME_MAPPINGS as PPS_FBG_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(PPS_FBG_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(PPS_FBG_DISPLAY_MAPPINGS)
    print("INFO: Successfully loaded PingPong Sampler (Custom V0.9.9 FBG).")
except Exception as e:
    print(f"WARNING: Could not load PingPongSampler_Custom_FBG: {e}")


try:
    from .SCENE_GENIUS_AUTOCREATOR import NODE_CLASS_MAPPINGS as SGC_CLASS_MAPPINGS
    from .SCENE_GENIUS_AUTOCREATOR import NODE_DISPLAY_NAME_MAPPINGS as SGC_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(SGC_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(SGC_DISPLAY_MAPPINGS)
except Exception as e:
    print(f"WARNING: Could not load SCENE_GENIUS_AUTOCREATOR: {e}")

try:
    from .Hybrid_Sigma_Scheduler import NODE_CLASS_MAPPINGS as HSS_CLASS_MAPPINGS
    from .Hybrid_Sigma_Scheduler import NODE_DISPLAY_NAME_MAPPINGS as HSS_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(HSS_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(HSS_DISPLAY_MAPPINGS)
except Exception as e:
    print(f"WARNING: Could not load Hybrid_Sigma_Scheduler: {e}")

# --- Import and add mappings from the 'latent' subdirectory ---
try:
    from .latent.ACE_LATENT_VISUALIZER import NODE_CLASS_MAPPINGS as ALV_CLASS_MAPPINGS
    from .latent.ACE_LATENT_VISUALIZER import NODE_DISPLAY_NAME_MAPPINGS as ALV_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(ALV_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(ALV_DISPLAY_MAPPINGS)
except Exception as e:
    print(f"WARNING: Could not load ACE_LATENT_VISUALIZER: {e}")

# --- Import and add mappings from the 'audio' subdirectory ---
try:
    from .audio.AdvancedAudioPreviewAndSave import NODE_CLASS_MAPPINGS as AAPS_CLASS_MAPPINGS
    from .audio.AdvancedAudioPreviewAndSave import NODE_DISPLAY_NAME_MAPPINGS as AAPS_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(AAPS_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(AAPS_DISPLAY_MAPPINGS)
except Exception as e:
    print(f"WARNING: Could not load AdvancedAudioPreviewAndSave: {e}")

try:
    from .audio.mastering_chain_node import NODE_CLASS_MAPPINGS as MCN_CLASS_MAPPINGS
    from .audio.mastering_chain_node import NODE_DISPLAY_NAME_MAPPINGS as MCN_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(MCN_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(MCN_DISPLAY_MAPPINGS)
except Exception as e:
    print(f"WARNING: Could not load mastering_chain_node: {e}")

# --- Add imports for the MD Seed Saver node ---
try:
    # Import the new Seed Saver node from the root of the MD_Nodes package
    from .seed_saver_node import NODE_CLASS_MAPPINGS as SS_CLASS_MAPPINGS
    from .seed_saver_node import NODE_DISPLAY_NAME_MAPPINGS as SS_DISPLAY_MAPPINGS
    NODE_CLASS_MAPPINGS.update(SS_CLASS_MAPPINGS)
    NODE_DISPLAY_NAME_MAPPINGS.update(SS_DISPLAY_MAPPINGS)
    print("INFO: Successfully loaded MD Seed Saver node.") # Updated print message
except Exception as e:
    print(f"WARNING: Could not load MD Seed Saver node: {e}")


# Define __all__ to explicitly expose what should be available when the package is imported
__all__ = [
    "NODE_CLASS_MAPPINGS",
    "NODE_DISPLAY_NAME_MAPPINGS",
    # You might have other entries here from your existing __all__ list.
]

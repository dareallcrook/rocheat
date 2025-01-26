import tkinter as tk
import json
import os

# Define the settings dictionaries for each button
esp_settings = {
    "FFlagDebugAvatarChatVisualization": "True",
    "FFlagEnableInGameMenuChromeABTest2": "False"
}

bunnyhop_settings = {
    "DFIntMaxAltitudePDStickHipHeightPercent": "-24"
}

wallhop_settings = {
    "DFIntAssemblyExtentsExpansionStudHundredth": -30
}

fakelag_settings = {
    "FFlagSimIslandizerManager": "false",
    "FFlagSimIslandizerManager": "false",
    "DFIntS2PhysicsSenderRate": "1",
    "DFFlagDebugVisualizationImprovements": "True",
    "DFFlagDebugVisualizeAllPropertyChanges": "True",
    "DFFlagDebugVisualizerTrackRotationPredictions": "True",
    "DFFlagDebugEnableInterpolationVisualizer": "True"
}

noclip_settings = {
    "DFIntAssemblyExtentsExpansionStudHundredth": -50
}

wallglide_settings = {
    "DFIntUnstickForceAttackInTenths": "-4"
}

jumper_settings = {
    "DFIntNewRunningBaseGravityReductionFactorHundredth": "1500"
}

tracker_settings = {
    "DFIntCSGLevelOfDetailSwitchingDistanceL12": "2",
    "FFlagDebugDisableTelemetryEphemeralCounter": "True",
    "DFIntClientPacketMaxDelayMs": "1",
    "DFIntPerformanceControlFrameTimeMax": "1",
    "DFIntAnimatorThrottleMaxFramesToSkip": "1",
    "FFlagEnableHasVerifiedBadgeUserModelValidation": "False",
    "FFlagDebugDisplayFPS": "False",
    "DFIntRaknetBandwidthInfluxHundredthsPercentageV2": "10000",
    "FFlagDebugDisableTelemetryV2Stat": "True",
    "DFIntReplicationDataCacheNumParallelTasks": "12",
    "DFIntNetworkSchemaCompressionRatio": "100",
    "DFIntClientPacketMaxFrameMicroseconds": "1000",
    "DFIntClientPacketExcessMicroseconds": "10000",
    "DFIntCSGLevelOfDetailSwitchingDistanceL34": "4",
    "DFIntMaxProcessPacketsJobScaling": "10000",
    "DFIntRakNetLoopMs": "0",
    "DFIntPerformanceControlFrameTimeMaxUtility": "-1",
    "DFIntS2PhysicsSenderRate": "38000",
    "DFIntClientPacketHealthyAllocationPercent": "15",
    "FFlagDisableChromeFollowupFTUX": "True",
    "DFFlagCreateMeshPartAtRuntime": "False",
    "FIntRuntimeMaxNumOfLatches": "4000000",
    "DFIntWaitOnUpdateNetworkLoopEndedMS": "100",
    "DFIntNumFramesAllowedToBeAboveError": "1",
    "DFIntPerformanceControlPredictedOOMAbsLimitExtraBufferMB": "1",
    "DFIntAnimationLodFacsDistanceMin": "0",
    "FIntTerrainArraySliceSize": "8",
    "FFlagDebugDisableTelemetryV2Event": "True",
    "FFlagEnableV3MenuABTest3": "False",
    "FFlagChromeBetaFeature": "False",
    "DFIntPerformanceControlSoundReloadLatencyMaxValue": "1",
    "DFIntAnimationLodFacsDistanceMax": "0",
    "FFlagFutureIsBrightPhase3Vulkan": "True",
    "DFIntPerformanceControlSoundReloadLatencyMinValue": "1",
    "DFIntLargePacketQueueSizeCutoffMB": "1000",
    "FIntSmoothClusterTaskQueueMaxParallelTasks": "12",
    "DFIntPerformanceControlSoundReloadLatencyTargetUtility": "1",
    "FIntRuntimeMaxNumOfThreads": "4000000",
    "FIntRakNetResendBufferArrayLength": "128",
    "DFFlagDebugPrintDataPingBreakDown": "False",
    "FFlagDebugForceFSMCPULightCulling": "True",
    "FFlagUserShowVerifiedBadgeInLegacyChat": "False",
    "DFIntMaxFrameBufferSize": "1",
    "FIntRobloxGuiBlurIntensity": "0",
    "FFlagDebugDisableTelemetryV2Counter": "True",
    "FFlagDebugDisableTelemetryPoint": "True",
    "FFlagFixGraphicsQuality": "True",
    "DFFlagDisableDPIScale": "True",
    "FFlagToolboxShowIdVerifiedFilter": "False",
    "DFIntBufferCompressionLevel": "0",
    "DFIntBufferCompressionThreshold": "100",
    "DFIntInitialAccelerationLatencyMultTenths": "1",
    "DFIntMaxAcceptableUpdateDelay": "0",
    "FFlagAvatarChatServiceExposeUserVerifiedForVoiceV2": "False",
    "DFIntAMPVerifiedTelemetryPointsHundredthsPercentage": "0",
    "DFIntAMPVerifiedTelemetryHundredthsPercentage": "0",
    "DFFlagAvatarChatServiceExposeUserVerifiedForVoiceMock": "False",
    "FIntRomarkStartWithGraphicQualityLevel": "1",
    "FFlagDisableChromeV3StaticSelfView": "True",
    "FFlagDisableChromeV3Icon": "True",
    "FFlagDisableChromeV3DockedMic": "True",
    "FFlagDisableChromeV3Captures": "True",
    "FFlagDisableChromeV3Baseline": "True",
    "FFlagDisableChromeUnibar": "True",
    "FFlagDebugDisableTelemetryEventIngest": "True",
    "DFFlagPreventReturnOfElevatedPhysicsFPS": "False",
    "FFlagDisableChromeFollowupUnibar": "True",
    "DFIntCSGLevelOfDetailSwitchingDistanceL23": "3",
    "FIntDebugForceMSAASamples": "1",
    "FIntFullscreenTitleBarTriggerDelayMillis": "18000000",
    "FFlagShowVerifiedBadgeOnDisplayNameBillboard": "False",
    "FFlagDebugForceFutureIsBrightPhase3": "True",
    "FIntFRMMinGrassDistance": "0",
    "FIntRuntimeMaxNumOfConditions": "4000000",
    "FIntRenderGrassDetailStrands": "0",
    "DFIntTimeBetweenSendConnectionAttemptsMS": "200",
    "FFlagTaskSchedulerLimitTargetFpsTo2402": "False",
    "DFIntTimestepArbiterThresholdCFLThou": "300",
    "FFlagDebugGraphicsPreferD3D11": "True",
    "FFlagPushFrameTimeToHarmony": "True",
    "FIntRuntimeMaxNumOfSchedulers": "4000000",
    "FFlagDebugEnableOctreeValidation": "False",
    "DFIntCSGLevelOfDetailSwitchingDistance": " 1",
    "DFIntPerformanceControlIXPQueueSizeUtilityExponentTenThousandths": "1",
    "DFIntPerformanceControlIXPQueueSizeBestUtility": "1",
    "DFIntPerformanceControlIXPBestQueueSize": "1",
    "DFIntDebugPerformanceControlUsedMemoryMB": "1",
    "DFFlagPerformanceControlIXPMemoryBufferConstantCheck": "True",
    "DFFlagPerformanceControlEnableMemoryProbing": "True",
    "DFFlagPerformanceControlEnableInference": "True",
    "DFFlagTextureQualityOverrideEnabled": "True",
    "DFIntTextureQualityOverride": "0",
    "DFIntDebugFRMQualityLevelOverride": "1",
    "FLogNetwork": "7"
}

# Create the main window
root = tk.Tk()
root.title("Settings GUI")

# Load settings from path.txt
def load_settings():
    settings_path = "path.txt"
    if os.path.exists(settings_path):
        with open(settings_path, "r") as f:
            path = f.read().strip()
        print("Path set to:", path)
        return path
    else:
        print("Path not set in path.txt")
        return None

# Save settings to path.txt
def save_settings(path):
    settings_path = "path.txt"
    with open(settings_path, "w") as f:
        f.write(path)
    print("Path saved to:", path)

# Load the path and display it
path = load_settings()
path_label = tk.Label(root, text=f"Path: {path}" if path else "Path not set")
path_label.pack()

# Toggle setting functions
def toggle_setting(setting_name, button, settings):
    if setting_name not in settings:
        settings[setting_name] = "True"
        button.config(bg="green", text=f"{setting_name}: Enabled")
    else:
        del settings[setting_name]
        button.config(bg="red", text=f"{setting_name}: Disabled")

# Create buttons for each setting
esp_button = tk.Button(root, text="ESP: Disabled", bg="red", command=lambda: toggle_setting("esp", esp_button, esp_settings))
esp_button.pack()

bunnyhop_button = tk.Button(root, text="Bunnyhop: Disabled", bg="red", command=lambda: toggle_setting("bunnyhop", bunnyhop_button, bunnyhop_settings))
bunnyhop_button.pack()

wallhop_button = tk.Button(root, text="Wallhop: Disabled", bg="red", command=lambda: toggle_setting("wallhop", wallhop_button, wallhop_settings))
wallhop_button.pack()

fakelag_button = tk.Button(root, text="Fakelag: Disabled", bg="red", command=lambda: toggle_setting("fakelag", fakelag_button, fakelag_settings))
fakelag_button.pack()

noclip_button = tk.Button(root, text="Noclip: Disabled", bg="red", command=lambda: toggle_setting("noclip", noclip_button, noclip_settings))
noclip_button.pack()

wallglide_button = tk.Button(root, text="Wallglide: Disabled", bg="red", command=lambda: toggle_setting("wallglide", wallglide_button, wallglide_settings))
wallglide_button.pack()

jumper_button = tk.Button(root, text="Jumper: Disabled", bg="red", command=lambda: toggle_setting("jumper", jumper_button, jumper_settings))
jumper_button.pack()

tracker_button = tk.Button(root, text="Tracker: Disabled", bg="red", command=lambda: toggle_setting("tracker", tracker_button, tracker_settings))
tracker_button.pack()

# Save button to save the path
save_button = tk.Button(root, text="Save Path", command=lambda: save_settings(path))
save_button.pack()

# Run the Tkinter main loop
root.mainloop()

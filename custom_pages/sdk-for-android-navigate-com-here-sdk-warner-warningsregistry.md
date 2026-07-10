---
title: "WarningsRegistry (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-warner-warningsregistry"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-warner-package-summary">com.here.sdk.warner</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.warner.WarningsRegistry → com.here.NativeBase com.here.sdk.warner.WarningsRegistry → com.here.sdk.warner.WarningsRegistry

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">WarningsRegistry</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

A class that store warning metadata for different warning types. Aggregates individual collection for each warning category (safety cameras, truck restrictions, etc.). Provided by WarnerEngine so callers can lookup detailed information about specific warnings. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

</div>

</div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">`BorderCrossingWarning`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getBorderCrossingWarning ( Warning warning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a border crossing warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-warner-customwarning" title="class in com.here.sdk.warner">`CustomWarning`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getCustomWarning ( Warning warning)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns additional data associated with the given custom warning.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarning" title="class in com.here.sdk.navigation">`DangerZoneWarning`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDangerZoneWarning ( Warning warning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a danger zone warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarning" title="class in com.here.sdk.navigation">`EnvironmentalZoneWarning`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getEnvironmentalZoneWarning ( Warning warning)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns environmental zone warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning" title="class in com.here.sdk.warner">`LaneDecreaseWarning`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLaneDecreaseWarning ( Warning warning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a lane decrease warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">`LowSpeedZoneWarning`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLowSpeedZoneWarning ( Warning warning)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a low speed zone warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarning" title="class in com.here.sdk.navigation">`RailwayCrossingWarning`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRailwayCrossingWarning ( Warning warning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a railway crossing warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation">`RealisticViewWarning`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRealisticViewWarning ( Warning warning)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a realistic-view warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning" title="class in com.here.sdk.navigation">`RoadSignWarning`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getRoadSignWarning ( Warning warning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a road-sign warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarning" title="class in com.here.sdk.navigation">`SafetyCameraWarning`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSafetyCameraWarning ( Warning warning)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a safety-camera warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarning" title="class in com.here.sdk.navigation">`SchoolZoneWarning`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getSchoolZoneWarning ( Warning warning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a school zone warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstop" title="class in com.here.sdk.navigation">`TollStop`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTollStopWarning ( Warning warning)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a toll stop warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning" title="class in com.here.sdk.navigation">`TrafficMergeWarning`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTrafficMergeWarning ( Warning warning)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a traffic merge warning corresponding to the given identifier.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning" title="class in com.here.sdk.navigation">`TruckRestrictionWarning`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTruckRestrictionWarning ( Warning warning)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns a truck restrictions warning corresponding to the given identifier.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getSafetyCameraWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getSafetyCameraWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarning" title="class in com.here.sdk.navigation">SafetyCameraWarning</a></span> <span class="element-name">getSafetyCameraWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a safety-camera warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single safety-camera warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-safetycamerawarning" title="class in com.here.sdk.navigation">`SafetyCameraWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getTruckRestrictionWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getTruckRestrictionWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning" title="class in com.here.sdk.navigation">TruckRestrictionWarning</a></span> <span class="element-name">getTruckRestrictionWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a truck restrictions warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single truck restrictions warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-truckrestrictionwarning" title="class in com.here.sdk.navigation">`TruckRestrictionWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getRoadSignWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getRoadSignWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-roadsignwarning" title="class in com.here.sdk.navigation">RoadSignWarning</a></span> <span class="element-name">getRoadSignWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a road-sign warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single road sign warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The `sdk.navigation.RoadSignWarning` object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getRealisticViewWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getRealisticViewWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation">RealisticViewWarning</a></span> <span class="element-name">getRealisticViewWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a realistic-view warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single realistic-view warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-realisticviewwarning" title="class in com.here.sdk.navigation">`RealisticViewWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getEnvironmentalZoneWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getEnvironmentalZoneWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarning" title="class in com.here.sdk.navigation">EnvironmentalZoneWarning</a></span> <span class="element-name">getEnvironmentalZoneWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns environmental zone warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single environmental zone warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-environmentalzonewarning" title="class in com.here.sdk.navigation">`EnvironmentalZoneWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getSchoolZoneWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getSchoolZoneWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarning" title="class in com.here.sdk.navigation">SchoolZoneWarning</a></span> <span class="element-name">getSchoolZoneWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a school zone warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single school zone warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-schoolzonewarning" title="class in com.here.sdk.navigation">`SchoolZoneWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getTollStopWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getTollStopWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstop" title="class in com.here.sdk.navigation">TollStop</a></span> <span class="element-name">getTollStopWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a toll stop warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single toll stop warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-tollstop" title="class in com.here.sdk.navigation">`TollStop`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getDangerZoneWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getDangerZoneWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarning" title="class in com.here.sdk.navigation">DangerZoneWarning</a></span> <span class="element-name">getDangerZoneWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a danger zone warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single danger zone warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-dangerzonewarning" title="class in com.here.sdk.navigation">`DangerZoneWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getBorderCrossingWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getBorderCrossingWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">BorderCrossingWarning</a></span> <span class="element-name">getBorderCrossingWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a border crossing warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single border crossing warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-bordercrossingwarning" title="class in com.here.sdk.navigation">`BorderCrossingWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getRailwayCrossingWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getRailwayCrossingWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarning" title="class in com.here.sdk.navigation">RailwayCrossingWarning</a></span> <span class="element-name">getRailwayCrossingWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a railway crossing warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single railway crossing warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-railwaycrossingwarning" title="class in com.here.sdk.navigation">`RailwayCrossingWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getLowSpeedZoneWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getLowSpeedZoneWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">LowSpeedZoneWarning</a></span> <span class="element-name">getLowSpeedZoneWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a low speed zone warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single low speed zone warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The <a href="sdk-for-android-navigate-com-here-sdk-navigation-lowspeedzonewarning" title="class in com.here.sdk.navigation">`LowSpeedZoneWarning`</a> object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getTrafficMergeWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getTrafficMergeWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-trafficmergewarning" title="class in com.here.sdk.navigation">TrafficMergeWarning</a></span> <span class="element-name">getTrafficMergeWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a traffic merge warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single traffic merge warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The `sdk.navigation.TrafficMergeWarning` object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning.

    </div>

  - <div id="sdk-for-android-navigate-getLaneDecreaseWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getLaneDecreaseWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-lanedecreasewarning" title="class in com.here.sdk.warner">LaneDecreaseWarning</a></span> <span class="element-name">getLaneDecreaseWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns a lane decrease warning corresponding to the given identifier.

    </div>

    Parameters:  
    `warning` -

    The identifier of the warning, as provided by `WarningListener.onWarning`. The `warning` uniquely identifies a single lane decrease warning within this registry and is used to retrieve its full metadata.

    Returns:  
    The `LaneDecreaseWarning` object associated with the provided `warning`, or `null` if no warning exists for the given `warning`. This object contains the full details and attributes of the corresponding warning. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  - <div id="sdk-for-android-navigate-getCustomWarning-com-here-sdk-warner-Warning" class="section detail">

    ### getCustomWarning

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-warner-customwarning" title="class in com.here.sdk.warner">CustomWarning</a></span> <span class="element-name">getCustomWarning</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">Warning</a> warning)</span>

    </div>

    <div class="block">

    Returns additional data associated with the given custom warning. The provided warning identifies a specific custom warning instance by its base warning information and custom warning type. This information is used to resolve the corresponding entry in the warning registry and retrieve any additional, type-specific data associated with the warning.

    </div>

    Parameters:  
    `warning` -

    The <a href="sdk-for-android-navigate-com-here-sdk-warner-warning" title="class in com.here.sdk.warner">`Warning`</a> instance identifying the custom warning for which additional data should be retrieved.

    Returns:  
    The `CustomWarning` associated with the given `warning`, or `null` if no additional data exists for this warning. The returned object contains the payload with type-specific details and attributes of the corresponding warning. **Note:** This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


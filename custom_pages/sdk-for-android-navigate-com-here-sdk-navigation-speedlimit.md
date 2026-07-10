---
title: "SpeedLimit (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-speedlimit"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.navigation.SpeedLimit → com.here.sdk.navigation.SpeedLimit

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">SpeedLimit</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents the speed limit of the current road. Speed limits that are described as conditional can be time-dependent. For time-dependent speed limits, the HERE SDK internally reads the current device time and notifies only on speed limits that are currently active. It is recommended to use effectiveSpeedLimitInMetersPerSecond() when an application does not offer dedicated speed limit indicators for other cases, such as weather-dependent speed limits.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#advisorySpeedLimitInMetersPerSecond" class="member-name-link"><code>advisorySpeedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A recommended speed limit that may not be indicated on the local road signs, but that serves to warn a driver that the road conditions may indicate a lower speed.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#fogSpeedLimitInMetersPerSecond" class="member-name-link"><code>fogSpeedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A conditional speed limit as indicated on the local road signs.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#optimalWeatherSpeedLimitInMetersPerSecond" class="member-name-link"><code>optimalWeatherSpeedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A conditional speed limit as indicated on the local road signs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#rainSpeedLimitInMetersPerSecond" class="member-name-link"><code>rainSpeedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A conditional speed limit as indicated on the local road signs.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#schoolZoneSpeedLimitInMetersPerSecond" class="member-name-link"><code>schoolZoneSpeedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  A conditional speed limit as indicated on the local road signs.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#snowSpeedLimitInMetersPerSecond" class="member-name-link"><code>snowSpeedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A conditional speed limit as indicated on the local road signs.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#speedLimitInMetersPerSecond" class="member-name-link"><code>speedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Regular speed limit if available.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#timeDependentSpeedLimitInMetersPerSecond" class="member-name-link"><code>timeDependentSpeedLimitInMetersPerSecond</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  A conditional speed limit as indicated on the local road signs.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      SpeedLimit ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

  </div>

  </div>

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

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      effectiveSpeedLimitInMetersPerSecond ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Returns the effective (lowest) speed limit between speedLimitInMetersPerSecond , schoolZoneSpeedLimitInMetersPerSecond , timeDependentSpeedLimitInMetersPerSecond and optimalWeatherSpeedLimitInMetersPerSecond .

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals ( Object obj)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-speedLimitInMetersPerSecond" class="section detail">

    ### speedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">speedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    Regular speed limit if available. In case of unbounded speed limit, the value is zero. Note: When following a route, then this value will depend on the selected transport mode. For other speed limits, like weather-dependent speed limits only the value as shown on the local road sign is provided. It may not be applicable to all transport modes. For tracking mode (without following a route), the VehicleProfile is ignored and only the speed limit from the local road sign is provided or the regular speed limit for a particular type of road or area like regular inner-city speed limits.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-advisorySpeedLimitInMetersPerSecond" class="section detail">

    ### advisorySpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">advisorySpeedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    A recommended speed limit that may not be indicated on the local road signs, but that serves to warn a driver that the road conditions may indicate a lower speed. Typically, the road condition is a curved road or a ramp but it may be due to a narrow road, narrow bridge, intersecting road, drainage dip, etc. In some cases, the advisory sign is on a different road than the one for which it applies (this can happen with ramps). In this case, the advisory speed is indicated for the road for which it is intended, even if the sign is further than 50 meters from the particular road. Advisory speed signs due to construction are not included. A speed value is published for advisory signs. A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-snowSpeedLimitInMetersPerSecond" class="section detail">

    ### snowSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">snowSpeedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when there is snow on the road. A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-rainSpeedLimitInMetersPerSecond" class="section detail">

    ### rainSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">rainSpeedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when it is raining or there is water on the road. A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-fogSpeedLimitInMetersPerSecond" class="section detail">

    ### fogSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">fogSpeedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility decreases due to fog. A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-optimalWeatherSpeedLimitInMetersPerSecond" class="section detail">

    ### optimalWeatherSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">optimalWeatherSpeedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    A conditional speed limit as indicated on the local road signs. The road speed limit that is in effect only when the visibility is optimal due to weather conditions. A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit. Note: This speed limit is conditioned by factors not expressed by the other ones. For example, it may be a time-related speed limit or a vehicle-related one.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-schoolZoneSpeedLimitInMetersPerSecond" class="section detail">

    ### schoolZoneSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">schoolZoneSpeedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    A conditional speed limit as indicated on the local road signs. School zone signs are often placed to slow drivers before reaching an intersection where children are crossing. A possible usage example can be to show an icon on the device's screen containing both special speed limit value and a visual cue in order to warn the user about the conditional speed limit.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-timeDependentSpeedLimitInMetersPerSecond" class="section detail">

    ### timeDependentSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">timeDependentSpeedLimitInMetersPerSecond</span>

    </div>

    <div class="block">

    A conditional speed limit as indicated on the local road signs. Speed limit that is in effect considering the current local time provided by the device's clock.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### SpeedLimit

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">SpeedLimit</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-equals-java-lang-Object" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-hashCode" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a> in class <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="sdk-for-android-navigate-effectiveSpeedLimitInMetersPerSecond" class="section detail">

    ### effectiveSpeedLimitInMetersPerSecond

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">effectiveSpeedLimitInMetersPerSecond</span>()

    </div>

    <div class="block">

    Returns the effective (lowest) speed limit between speedLimitInMetersPerSecond , schoolZoneSpeedLimitInMetersPerSecond , timeDependentSpeedLimitInMetersPerSecond and optimalWeatherSpeedLimitInMetersPerSecond .

    </div>

    Returns:  
    Returns the lowest value between: <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#speedLimitInMetersPerSecond">`speedLimitInMetersPerSecond`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#schoolZoneSpeedLimitInMetersPerSecond">`schoolZoneSpeedLimitInMetersPerSecond`</a>, <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#timeDependentSpeedLimitInMetersPerSecond">`timeDependentSpeedLimitInMetersPerSecond`</a> and <a href="sdk-for-android-navigate-com-here-sdk-navigation-speedlimit#optimalWeatherSpeedLimitInMetersPerSecond">`optimalWeatherSpeedLimitInMetersPerSecond`</a>.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


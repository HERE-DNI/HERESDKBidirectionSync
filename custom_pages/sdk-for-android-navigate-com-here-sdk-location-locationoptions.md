---
title: "LocationOptions (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationoptions"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-location-package-summary">com.here.sdk.location</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.location.LocationOptions → com.here.sdk.location.LocationOptions

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">LocationOptions</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Location options that combine notification, sensor, cellular positioning, GNSS positioning and WiFi positioning options.

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

  <a href="sdk-for-android-navigate-com-here-sdk-location-cellularpositioningoptions" title="class in com.here.sdk.location">`CellularPositioningOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#cellularPositioningOptions" class="member-name-link"><code>cellularPositioningOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Cellular network positioning options.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-notificationoptions" title="class in com.here.sdk.location">`NotificationOptions`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#notificationOptions" class="member-name-link"><code>notificationOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Positioning notification options.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions" title="class in com.here.sdk.location">`SatellitePositioningOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#satellitePositioningOptions" class="member-name-link"><code>satellitePositioningOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  GNSS positioning options.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-sensoroptions" title="class in com.here.sdk.location">`SensorOptions`</a>

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#sensorOptions" class="member-name-link"><code>sensorOptions</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Positioning sensor options.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-wifipositioningoptions" title="class in com.here.sdk.location">`WifiPositioningOptions`</a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationoptions#wifiPositioningOptions" class="member-name-link"><code>wifiPositioningOptions</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  WiFi network positioning options.

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

      LocationOptions ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs LocationOptions from default options.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      LocationOptions ( LocationAccuracy locationAccuracy)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs LocationOptions from LocationAccuracy.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-notificationOptions" class="section detail">

    ### notificationOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-notificationoptions" title="class in com.here.sdk.location">NotificationOptions</a></span> <span class="element-name">notificationOptions</span>

    </div>

    <div class="block">

    Positioning notification options.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-sensorOptions" class="section detail">

    ### sensorOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-sensoroptions" title="class in com.here.sdk.location">SensorOptions</a></span> <span class="element-name">sensorOptions</span>

    </div>

    <div class="block">

    Positioning sensor options.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-cellularPositioningOptions" class="section detail">

    ### cellularPositioningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-cellularpositioningoptions" title="class in com.here.sdk.location">CellularPositioningOptions</a></span> <span class="element-name">cellularPositioningOptions</span>

    </div>

    <div class="block">

    Cellular network positioning options.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-satellitePositioningOptions" class="section detail">

    ### satellitePositioningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-satellitepositioningoptions" title="class in com.here.sdk.location">SatellitePositioningOptions</a></span> <span class="element-name">satellitePositioningOptions</span>

    </div>

    <div class="block">

    GNSS positioning options.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-wifiPositioningOptions" class="section detail">

    ### wifiPositioningOptions

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-wifipositioningoptions" title="class in com.here.sdk.location">WifiPositioningOptions</a></span> <span class="element-name">wifiPositioningOptions</span>

    </div>

    <div class="block">

    WiFi network positioning options.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init" class="section detail">

    ### LocationOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationOptions</span>()

    </div>

    <div class="block">

    Constructs LocationOptions from default options.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-location-LocationAccuracy" class="section detail">

    ### LocationOptions

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">LocationOptions</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-location-locationaccuracy" title="enum class in com.here.sdk.location">LocationAccuracy</a> locationAccuracy)</span>

    </div>

    <div class="block">

    Constructs LocationOptions from LocationAccuracy. Returned LocationOptions instance has default options for given LocationAccuracy set.

    </div>

    Parameters:  
    `locationAccuracy` -

    LocationAccuracy to define the LocationOptions.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


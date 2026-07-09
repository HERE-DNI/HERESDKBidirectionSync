---
title: "LocationIssueType (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-location-locationissuetype"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-location-package-summary">com.here.sdk.location</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object java.lang.Enum \< LocationIssueType \> com.here.sdk.location.LocationIssueType → java.lang.Enum \< LocationIssueType \> com.here.sdk.location.LocationIssueType → com.here.sdk.location.LocationIssueType

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

All Implemented Interfaces:  
<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/Serializable.html" class="external-link" title="class or interface in java.io"><code>Serializable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Comparable.html" class="external-link" title="class or interface in java.lang"><code>Comparable</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">`LocationIssueType`</a>`>`, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/constant/Constable.html" class="external-link" title="class or interface in java.lang.constant"><code>Constable</code></a>

<div class="type-signature">

<span class="modifiers">public enum </span><span class="element-name type-name-label">LocationIssueType</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>\<<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>\></span>

</div>

<div class="block">

Represents specific issues affecting location retrieval quality, availability, or functionality. Issues are detected automatically by the positioning system and reported via LocationIssueListener. Multiple issues may be active simultaneously (e.g., both quality degradation and connectivity problems). Issues clear automatically when underlying conditions improve (no manual dismissal needed).

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="inherited-list">

  ## Nested classes/interfaces inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>Enum.EnumDesc</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>` extends `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang"><code>Enum</code></a>`<`<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.EnumDesc.html" class="external-link" title="class or interface in java.lang"><code>E</code></a>`>>`

  </div>

  </div>

- <div id="sdk-for-android-navigate-enum-constant-summary" class="section constants-summary">

  ## Enum Constant Summary

  <div class="caption">

  Enum Constants

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Enum Constant

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#FEATURE_NOT_INCLUDED" class="member-name-link"><code>FEATURE_NOT_INCLUDED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Requested feature not available for the used license.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#FEATURE_NOT_LICENSED" class="member-name-link"><code>FEATURE_NOT_LICENSED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Requested feature requires a valid license (missing or expired).

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_CONNECTION_NOT_AVAILABLE" class="member-name-link"><code>HDGNSS_CONNECTION_NOT_AVAILABLE</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Network connection to HD GNSS assistance server is unavailable.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_DEGRADED_MEASUREMENT_QUALITY" class="member-name-link"><code>HDGNSS_DEGRADED_MEASUREMENT_QUALITY</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Satellite measurement quality is degraded; HD GNSS accuracy level may not be achieved.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_DEVICE_NOT_SUPPORTED" class="member-name-link"><code>HDGNSS_DEVICE_NOT_SUPPORTED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Device hardware does not support HD GNSS positioning capabilities.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY" class="member-name-link"><code>HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Satellite measurement quality is insufficient to achieve HD GNSS accuracy level.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_OS_VERSION_NOT_SUPPORTED" class="member-name-link"><code>HDGNSS_OS_VERSION_NOT_SUPPORTED</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Operating system version is below minimum required for HD GNSS (Android 12+).

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#HDGNSS_POS_EXTRAPOLATED" class="member-name-link"><code>HDGNSS_POS_EXTRAPOLATED</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Hd gnss position was calculated by extrapolation.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_CELL_SCAN_ERROR" class="member-name-link"><code>POSITION_CELL_SCAN_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Failed to scan for cellular network signals.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NO_CELL_MEASUREMENTS" class="member-name-link"><code>POSITION_NO_CELL_MEASUREMENTS</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  No usable cellular network signal measurements available for positioning.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NO_WLAN_MEASUREMENTS" class="member-name-link"><code>POSITION_NO_WLAN_MEASUREMENTS</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  No usable Wi-Fi network signal measurements available for positioning.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_NOT_FOUND" class="member-name-link"><code>POSITION_NOT_FOUND</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Unable to determine position from available positioning sources.

  </div>

  </div>

  <div class="col-first even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#POSITION_WLAN_SCAN_ERROR" class="member-name-link"><code>POSITION_WLAN_SCAN_ERROR</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Failed to scan for Wi-Fi network signals.

  </div>

  </div>

  <div class="col-first odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype#SENSOR_POSITIONING_NOT_AVAILABLE" class="member-name-link"><code>SENSOR_POSITIONING_NOT_AVAILABLE</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Device sensors required for sensor fusion positioning are unavailable.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">`LocationIssueType`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      valueOf ( String name)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns the enum constant of this class with the specified name.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">`LocationIssueType`</a>`[]`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      values ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Returns an array containing the constants of this enum class, in the order they are declared.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html" class="external-link" title="class or interface in java.lang">Enum</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#compareTo(E)" class="external-link" title="class or interface in java.lang"><code>compareTo</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#describeConstable()" class="external-link" title="class or interface in java.lang"><code>describeConstable</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#getDeclaringClass()" class="external-link" title="class or interface in java.lang"><code>getDeclaringClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#name()" class="external-link" title="class or interface in java.lang"><code>name</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#ordinal()" class="external-link" title="class or interface in java.lang"><code>ordinal</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Enum.html#valueOf(java.lang.Class,java.lang.String)" class="external-link" title="class or interface in java.lang"><code>valueOf</code></a>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-enum-constant-detail" class="section constant-details">

  ## Enum Constant Details

  - <div id="sdk-for-android-navigate-HDGNSS_DEVICE_NOT_SUPPORTED" class="section detail">

    ### HDGNSS_DEVICE_NOT_SUPPORTED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_DEVICE_NOT_SUPPORTED</span>

    </div>

    <div class="block">

    Device hardware does not support HD GNSS positioning capabilities.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-HDGNSS_OS_VERSION_NOT_SUPPORTED" class="section detail">

    ### HDGNSS_OS_VERSION_NOT_SUPPORTED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_OS_VERSION_NOT_SUPPORTED</span>

    </div>

    <div class="block">

    Operating system version is below minimum required for HD GNSS (Android 12+).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-HDGNSS_CONNECTION_NOT_AVAILABLE" class="section detail">

    ### HDGNSS_CONNECTION_NOT_AVAILABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_CONNECTION_NOT_AVAILABLE</span>

    </div>

    <div class="block">

    Network connection to HD GNSS assistance server is unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-HDGNSS_DEGRADED_MEASUREMENT_QUALITY" class="section detail">

    ### HDGNSS_DEGRADED_MEASUREMENT_QUALITY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_DEGRADED_MEASUREMENT_QUALITY</span>

    </div>

    <div class="block">

    Satellite measurement quality is degraded; HD GNSS accuracy level may not be achieved.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY" class="section detail">

    ### HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_INSUFFICIENT_MEASUREMENT_QUALITY</span>

    </div>

    <div class="block">

    Satellite measurement quality is insufficient to achieve HD GNSS accuracy level.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-FEATURE_NOT_LICENSED" class="section detail">

    ### FEATURE_NOT_LICENSED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">FEATURE_NOT_LICENSED</span>

    </div>

    <div class="block">

    Requested feature requires a valid license (missing or expired).

    </div>

    </div>

  - <div id="sdk-for-android-navigate-FEATURE_NOT_INCLUDED" class="section detail">

    ### FEATURE_NOT_INCLUDED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">FEATURE_NOT_INCLUDED</span>

    </div>

    <div class="block">

    Requested feature not available for the used license.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-SENSOR_POSITIONING_NOT_AVAILABLE" class="section detail">

    ### SENSOR_POSITIONING_NOT_AVAILABLE

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">SENSOR_POSITIONING_NOT_AVAILABLE</span>

    </div>

    <div class="block">

    Device sensors required for sensor fusion positioning are unavailable.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-POSITION_NOT_FOUND" class="section detail">

    ### POSITION_NOT_FOUND

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_NOT_FOUND</span>

    </div>

    <div class="block">

    Unable to determine position from available positioning sources.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-POSITION_NO_CELL_MEASUREMENTS" class="section detail">

    ### POSITION_NO_CELL_MEASUREMENTS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_NO_CELL_MEASUREMENTS</span>

    </div>

    <div class="block">

    No usable cellular network signal measurements available for positioning.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-POSITION_NO_WLAN_MEASUREMENTS" class="section detail">

    ### POSITION_NO_WLAN_MEASUREMENTS

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_NO_WLAN_MEASUREMENTS</span>

    </div>

    <div class="block">

    No usable Wi-Fi network signal measurements available for positioning.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-POSITION_CELL_SCAN_ERROR" class="section detail">

    ### POSITION_CELL_SCAN_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_CELL_SCAN_ERROR</span>

    </div>

    <div class="block">

    Failed to scan for cellular network signals.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-POSITION_WLAN_SCAN_ERROR" class="section detail">

    ### POSITION_WLAN_SCAN_ERROR

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">POSITION_WLAN_SCAN_ERROR</span>

    </div>

    <div class="block">

    Failed to scan for Wi-Fi network signals.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-HDGNSS_POS_EXTRAPOLATED" class="section detail">

    ### HDGNSS_POS_EXTRAPOLATED

    <div class="member-signature">

    <span class="modifiers">public static final</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">HDGNSS_POS_EXTRAPOLATED</span>

    </div>

    <div class="block">

    Hd gnss position was calculated by extrapolation.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-values" class="section detail">

    ### values

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a>\[\]</span> <span class="element-name">values</span>()

    </div>

    <div class="block">

    Returns an array containing the constants of this enum class, in the order they are declared.

    </div>

    Returns:  
    an array containing the constants of this enum class, in the order they are declared

    </div>

  - <div id="sdk-for-android-navigate-valueOf-java-lang-String" class="section detail">

    ### valueOf

    <div class="member-signature">

    <span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-location-locationissuetype" title="enum class in com.here.sdk.location">LocationIssueType</a></span> <span class="element-name">valueOf</span><wbr></wbr><span class="parameters">(<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Returns the enum constant of this class with the specified name. The string must match exactly an identifier used to declare an enum constant in this class. (Extraneous whitespace characters are not permitted.)

    </div>

    Parameters:  
    `name` - the name of the enum constant to be returned.

    Returns:  
    the enum constant with the specified name

    Throws:  
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/IllegalArgumentException.html" class="external-link" title="class or interface in java.lang"><code>IllegalArgumentException</code></a> - if this enum class has no constant with the specified name

    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/NullPointerException.html" class="external-link" title="class or interface in java.lang"><code>NullPointerException</code></a> - if the argument is null

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


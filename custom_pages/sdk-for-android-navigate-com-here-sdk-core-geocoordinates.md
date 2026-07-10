---
title: "GeoCoordinates (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-core-geocoordinates"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-core-package-summary">com.here.sdk.core</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.core.GeoCoordinates → com.here.sdk.core.GeoCoordinates

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">GeoCoordinates</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents geographical coordinates in 3D space.

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

  `final `<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#altitude" class="member-name-link"><code>altitude</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional altitude in meters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final double`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#latitude" class="member-name-link"><code>latitude</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Latitude in degrees.

  </div>

  </div>

  <div class="col-first even-row-color">

  `final double`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates#longitude" class="member-name-link"><code>longitude</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Longitude in degrees.

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

      GeoCoordinates (double latitude,
       double longitude)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a GeoCoordinates from the provided latitude and longitude values.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GeoCoordinates (double latitude,
       double longitude,
       double altitude)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a GeoCoordinates from the provided latitude, longitude and altitude values.

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

  `double`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      distanceTo ( GeoCoordinates point)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Computes distance (in meters) along the great circle between two coordinates.

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

  <div class="col-first even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromString ( String input)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Constructs GeoCoordinates from the provided string in specified format.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">`GeoCoordinates`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      interpolate ( GeoCoordinates towardCoords,
       double factor)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Computes the coordinates of the interpolated location along the great circle between the two coordinates.

  </div>

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

  - <div id="sdk-for-android-navigate-latitude" class="section detail">

    ### latitude

    <div class="member-signature">

    <span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">latitude</span>

    </div>

    <div class="block">

    Latitude in degrees.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-longitude" class="section detail">

    ### longitude

    <div class="member-signature">

    <span class="modifiers">public final</span> <span class="return-type">double</span> <span class="element-name">longitude</span>

    </div>

    <div class="block">

    Longitude in degrees.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-altitude" class="section detail">

    ### altitude

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public final</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html" class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">altitude</span>

    </div>

    <div class="block">

    Optional altitude in meters. By convention, on iOS devices, altitude is set as meters relative to the mean sea level. On Android devices, altitude is set as meters relative to the WGS 84 reference ellipsoid.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-double-double-double" class="section detail">

    ### GeoCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoCoordinates</span><wbr></wbr><span class="parameters">(double latitude, double longitude, double altitude)</span>

    </div>

    <div class="block">

    Constructs a GeoCoordinates from the provided latitude, longitude and altitude values. Corrects values of lat and long if they exceed the ranges.

    </div>

    Parameters:  
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to 0.0.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to 0.0.

    `altitude` -

    Altitude in meters. NaN value is converted to `null`.

    </div>

  - <div id="sdk-for-android-navigate-init-double-double" class="section detail">

    ### GeoCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoCoordinates</span><wbr></wbr><span class="parameters">(double latitude, double longitude)</span>

    </div>

    <div class="block">

    Constructs a GeoCoordinates from the provided latitude and longitude values. Corrects values of latitude and longitude if they exceed the ranges. Altitude set to null .

    </div>

    Parameters:  
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If the value is out of range of \[-90.0, 90.0\] it's clamped to that range. NaN value is converted to 0.0.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If the value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. NaN value is converted to 0.0.

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

  - <div id="sdk-for-android-navigate-distanceTo-com-here-sdk-core-GeoCoordinates" class="section detail">

    ### distanceTo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceTo</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> point)</span>

    </div>

    <div class="block">

    Computes distance (in meters) along the great circle between two coordinates. This method ignores altitude of both points.

    </div>

    Parameters:  
    `point` -

    Coordinates of the point to which the distance is computed.

    Returns:  
    distance in meters.

    </div>

  - <div id="sdk-for-android-navigate-interpolate-com-here-sdk-core-GeoCoordinates-double" class="section detail">

    ### interpolate

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">interpolate</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a> towardCoords, double factor)</span>

    </div>

    <div class="block">

    Computes the coordinates of the interpolated location along the great circle between the two coordinates. The interpolation factor is clamped to the range \[0.0, 1.0\] where 0.0 identifies this GeoCoordinates and 1.0 indicates the other coordinates. The ratio between the distance to the interpolated coordinates and the distance to the other coordinates is approximately equal to the interpolation factor. When both coordinates have the altitude, then the altitude is interpolated as well; null otherwise.

    </div>

    Parameters:  
    `towardCoords` -

    Coordinates of the point to which the interpolation is directed.

    `factor` -

    The interpolation factor

    Returns:  
    interpolated coordinates

    </div>

  - <div id="sdk-for-android-navigate-fromString-java-lang-String" class="section detail">

    ### fromString

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geocoordinates" title="class in com.here.sdk.core">GeoCoordinates</a></span> <span class="element-name">fromString</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> input)</span>

    </div>

    <div class="block">

    Constructs GeoCoordinates from the provided string in specified format. Corrects values of lat and long if they exceed the ranges. If the latitude value is out of range of \[-90.0, 90.0\] it's clamped to that range. If the longitude value is out of range of \[-180.0, 180.0\] it's replaced with a value within the range, representing effectively the same meridian. Examples: 53.43762,-13.65468 . 49°59'56.948"N, 15°48'22.989"E 50d4m17.698N 14d24m2.826E 49.9991522N, 150.8063858E 40°26′47″N 79°58′36″W

    </div>

    Parameters:  
    `input` -

    String representing GeoCoordinates in one of supported formats.

    Returns:  
    Created GeoCoordinates, or 'null' if string was not in appropriate format.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


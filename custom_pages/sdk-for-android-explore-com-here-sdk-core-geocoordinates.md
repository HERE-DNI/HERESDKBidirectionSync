---
title: "GeoCoordinates (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geocoordinates"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.GeoCoordinates

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">GeoCoordinates</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents geographical coordinates in 3D space.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates#altitude"
  class="member-name-link"><code>altitude</code></a></td>
  <td><div class="block">
  Optional altitude in meters.
  </div></td>
  </tr>
  <tr>
  <td><code>final double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates#latitude"
  class="member-name-link"><code>latitude</code></a></td>
  <td><div class="block">
  Latitude in degrees.
  </div></td>
  </tr>
  <tr>
  <td><code>final double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates#longitude"
  class="member-name-link"><code>longitude</code></a></td>
  <td><div class="block">
  Longitude in degrees.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>GeoCoordinates(double latitude,
   double longitude)</code></pre></td>
  <td><div class="block">
  Constructs a GeoCoordinates from the provided latitude and longitude
  values.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>GeoCoordinates(double latitude,
   double longitude,
   double altitude)</code></pre></td>
  <td><div class="block">
  Constructs a GeoCoordinates from the provided latitude, longitude and
  altitude values.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
  Static Methods
  Instance Methods
  Concrete Methods

  </div>

  <div id="method-summary-table.tabpanel"
  aria-labelledby="method-summary-table-tab0" role="tabpanel">

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Method</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>double</code></td>
  <td><pre><code>distanceTo(GeoCoordinates point)</code></pre></td>
  <td><div class="block">
  Computes distance (in meters) along the great circle between two
  coordinates.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>static </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><pre><code>fromString(String input)</code></pre></td>
  <td><div class="block">
  Constructs GeoCoordinates from the provided string in specified format.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><pre><code>interpolate(GeoCoordinates towardCoords,
   double factor)</code></pre></td>
  <td><div class="block">
  Computes the coordinates of the interpolated location along the great
  circle between the two coordinates.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="latitude" class="section detail">

    ### latitude

    <div class="member-signature">

    <span class="modifiers">public
    final</span> <span class="return-type">double</span> <span class="element-name">latitude</span>

    </div>

    <div class="block">

    Latitude in degrees.

    </div>

    </div>

  - <div id="longitude" class="section detail">

    ### longitude

    <div class="member-signature">

    <span class="modifiers">public
    final</span> <span class="return-type">double</span> <span class="element-name">longitude</span>

    </div>

    <div class="block">

    Longitude in degrees.

    </div>

    </div>

  - <div id="altitude" class="section detail">

    ### altitude

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">altitude</span>

    </div>

    <div class="block">

    Optional altitude in meters. By convention, on iOS devices, altitude
    is set as meters relative to the mean sea level. On Android devices,
    altitude is set as meters relative to the WGS 84 reference
    ellipsoid.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(double,double,double)" class="section detail">

    ### GeoCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoCoordinates</span><span class="parameters">(double latitude,
    double longitude, double altitude)</span>

    </div>

    <div class="block">

    Constructs a GeoCoordinates from the provided latitude, longitude
    and altitude values. Corrects values of lat and long if they exceed
    the ranges.

    </div>

    Parameters:  
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If
    the value is out of range of \[-90.0, 90.0\] it's clamped to that
    range. NaN value is converted to 0.0.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If
    the value is out of range of \[-180.0, 180.0\] it's replaced with a
    value within the range, representing effectively the same meridian.
    NaN value is converted to 0.0.

    `altitude` -

    Altitude in meters. NaN value is converted to `null`.

    </div>

  - <div id="<init>(double,double)" class="section detail">

    ### GeoCoordinates

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoCoordinates</span><span class="parameters">(double latitude,
    double longitude)</span>

    </div>

    <div class="block">

    Constructs a GeoCoordinates from the provided latitude and longitude
    values. Corrects values of latitude and longitude if they exceed the
    ranges. Altitude set to null .

    </div>

    Parameters:  
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If
    the value is out of range of \[-90.0, 90.0\] it's clamped to that
    range. NaN value is converted to 0.0.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If
    the value is out of range of \[-180.0, 180.0\] it's replaced with a
    value within the range, representing effectively the same meridian.
    NaN value is converted to 0.0.

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="equals(java.lang.Object)" class="section detail">

    ### equals

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">equals</span><span class="parameters">(<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link" title="class or interface in java.lang">Object</a> obj)</span>

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
    class="external-link"
    title="class or interface in java.lang"><code>equals</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="hashCode()" class="section detail">

    ### hashCode

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">hashCode</span>()

    </div>

    Overrides:  
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
    class="external-link"
    title="class or interface in java.lang"><code>hashCode</code></a> in
    class <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
    class="external-link"
    title="class or interface in java.lang"><code>Object</code></a>

    </div>

  - <div id="distanceTo(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### distanceTo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">distanceTo</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") point)</span>

    </div>

    <div class="block">

    Computes distance (in meters) along the great circle between two
    coordinates. This method ignores altitude of both points.

    </div>

    Parameters:  
    `point` -

    Coordinates of the point to which the distance is computed.

    Returns:  
    distance in meters.

    </div>

  - <div id="interpolate(com.here.sdk.core.GeoCoordinates,double)"
    class="section detail">

    ### interpolate

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">interpolate</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") towardCoords,
    double factor)</span>

    </div>

    <div class="block">

    Computes the coordinates of the interpolated location along the
    great circle between the two coordinates. The interpolation factor
    is clamped to the range \[0.0, 1.0\] where 0.0 identifies this
    GeoCoordinates and 1.0 indicates the other coordinates. The ratio
    between the distance to the interpolated coordinates and the
    distance to the other coordinates is approximately equal to the
    interpolation factor. When both coordinates have the altitude, then
    the altitude is interpolated as well; null otherwise.

    </div>

    Parameters:  
    `towardCoords` -

    Coordinates of the point to which the interpolation is directed.

    `factor` -

    The interpolation factor

    Returns:  
    interpolated coordinates

    </div>

  - <div id="fromString(java.lang.String)" class="section detail">

    ### fromString

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    static</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">fromString</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> input)</span>

    </div>

    <div class="block">

    Constructs GeoCoordinates from the provided string in specified
    format. Corrects values of lat and long if they exceed the ranges.
    If the latitude value is out of range of \[-90.0, 90.0\] it's
    clamped to that range. If the longitude value is out of range of
    \[-180.0, 180.0\] it's replaced with a value within the range,
    representing effectively the same meridian. Examples:
    53.43762,-13.65468 . 49°59'56.948"N, 15°48'22.989"E 50d4m17.698N
    14d24m2.826E 49.9991522N, 150.8063858E 40°26′47″N 79°58′36″W

    </div>

    Parameters:  
    `input` -

    String representing GeoCoordinates in one of supported formats.

    Returns:  
    Created GeoCoordinates, or 'null' if string was not in appropriate
    format.

    </div>

  </div>

</div>


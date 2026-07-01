---
title: "GeoCoordinatesUpdate (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.GeoCoordinatesUpdate

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">GeoCoordinatesUpdate</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents geographical coordinates in 3D space. Unlike GeoCoordinates ,
its members can be undefined, allowing for APIs that update only the
specified parts of geo coordinates.

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
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate#altitude"
  class="member-name-link"><code>altitude</code></a></td>
  <td><div class="block">
  Optional altitude in meters.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate#latitude"
  class="member-name-link"><code>latitude</code></a></td>
  <td><div class="block">
  Optional latitude in degrees.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate#longitude"
  class="member-name-link"><code>longitude</code></a></td>
  <td><div class="block">
  Optional longitude in degrees.
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
  <td><pre><code>GeoCoordinatesUpdate(GeoCoordinates coordinates)</code></pre></td>
  <td><div class="block">
  Constructs a GeoCoordinatesUpdate from GeoCoordinates
  </div></td>
  </tr>
  <tr>
  <td><pre><code>GeoCoordinatesUpdate(Double latitude,
   Double longitude)</code></pre></td>
  <td><div class="block">
  Constructs a GeoCoordinatesUpdate from the provided latitude and
  longitude values.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>GeoCoordinatesUpdate(Double latitude,
   Double longitude,
   Double altitude)</code></pre></td>
  <td><div class="block">
  Constructs a GeoCoordinatesUpdate from the provided latitude, longitude
  and alt values.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div id="method-summary-table">

  <div class="table-tabs" aria-orientation="horizontal" role="tablist">

  All Methods
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
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><pre><code>hashCode()</code></pre></td>
  <td> </td>
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

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">latitude</span>

    </div>

    <div class="block">

    Optional latitude in degrees.

    </div>

    </div>

  - <div id="longitude" class="section detail">

    ### longitude

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a></span> <span class="element-name">longitude</span>

    </div>

    <div class="block">

    Optional longitude in degrees.

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

    Optional altitude in meters.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.lang.Double,java.lang.Double)"
    class="section detail">

    ### GeoCoordinatesUpdate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoCoordinatesUpdate</span><span class="parameters">(@Nullable
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> latitude,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> longitude)</span>

    </div>

    <div class="block">

    Constructs a GeoCoordinatesUpdate from the provided latitude and
    longitude values. Corrects values of latitude and longitude if they
    exceed the ranges.

    </div>

    Parameters:  
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If
    the value is out of range of \[-90.0, 90.0\] it's clamped to that
    range. NaN value is converted to `null`.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If
    the value is out of range of \[-180.0, 180.0\] it's replaced with a
    value within the range, representing effectively the same meridian.
    NaN value is converted to `null`.

    </div>

  - <div id="<init>(java.lang.Double,java.lang.Double,java.lang.Double)"
    class="section detail">

    ### GeoCoordinatesUpdate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoCoordinatesUpdate</span><span class="parameters">(@Nullable
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> latitude,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> longitude,
    @Nullable <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a> altitude)</span>

    </div>

    <div class="block">

    Constructs a GeoCoordinatesUpdate from the provided latitude,
    longitude and alt values. Corrects values of latitude and longitude
    if they exceed the ranges.

    </div>

    Parameters:  
    `latitude` -

    Latitude in degrees. Positive value means Northern hemisphere. If
    the value is out of range of \[-90.0, 90.0\] it's clamped to that
    range. NaN value is converted to `null`.

    `longitude` -

    Longitude in degrees. Positive value means Eastern hemisphere. If
    the value is out of range of \[-180.0, 180.0\] it's replaced with a
    value within the range, representing effectively the same meridian.
    NaN value is converted to `null`.

    `altitude` -

    Altitude in meters. NaN value is converted to `null`.

    </div>

  - <div id="<init>(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### GeoCoordinatesUpdate

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoCoordinatesUpdate</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") coordinates)</span>

    </div>

    <div class="block">

    Constructs a GeoCoordinatesUpdate from GeoCoordinates

    </div>

    Parameters:  
    `coordinates` -

    GeoCoordinates to construct GeoCoordinatesUpdate.

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

  </div>

</div>


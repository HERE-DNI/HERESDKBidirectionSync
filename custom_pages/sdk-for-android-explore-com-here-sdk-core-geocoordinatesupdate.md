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

<div id="sdk-for-android-explore-class-description"
class="section class-description">

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
<div id="sdk-for-android-explore-field-summary"
  class="section field-summary">

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

  `final `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate#altitude"
  class="member-name-link"><code>altitude</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional altitude in meters.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate#latitude"
  class="member-name-link"><code>latitude</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Optional latitude in degrees.

  </div>

  </div>

  <div class="col-first even-row-color">

  `final `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinatesupdate#longitude"
  class="member-name-link"><code>longitude</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Optional longitude in degrees.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      GeoCoordinatesUpdate(GeoCoordinates coordinates)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a GeoCoordinatesUpdate from GeoCoordinates

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GeoCoordinatesUpdate(Double latitude,
       Double longitude)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a GeoCoordinatesUpdate from the provided latitude and
  longitude values.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      GeoCoordinatesUpdate(Double latitude,
       Double longitude,
       Double altitude)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a GeoCoordinatesUpdate from the provided latitude,
  longitude and alt values.

  </div>

  </div>

  </div>

  </div>
<div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

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

  `boolean`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      equals(Object obj)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `int`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      hashCode()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

   

  </div>

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
<div id="sdk-for-android-explore-field-detail"
  class="section field-details">
<div id="sdk-for-android-explore-latitude" class="section detail">

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
<div id="sdk-for-android-explore-longitude" class="section detail">

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
<div id="sdk-for-android-explore-altitude" class="section detail">

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
<div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">
<div id="sdk-for-android-explore-<init>(java.lang.Double,java.lang.Double)"
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
<div id="sdk-for-android-explore-<init>(java.lang.Double,java.lang.Double,java.lang.Double)"
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
<div id="sdk-for-android-explore-<init>(com.here.sdk.core.GeoCoordinates)"
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
<div id="sdk-for-android-explore-method-detail"
  class="section method-details">
<div id="sdk-for-android-explore-equals(java.lang.Object)"
    class="section detail">

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
<div id="sdk-for-android-explore-hashCode()" class="section detail">

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


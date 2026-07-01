---
title: "GeoPolyline (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geopolyline"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.GeoPolyline

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">GeoPolyline</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

A list of geographic coordinates representing the vertices of a
polyline. An instance of this class, initialized with appropriate
vertices. Represents a GeoPolyline as a series of geographic
coordinates.

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geopolyline#vertices"
  class="member-name-link"><code>vertices</code></a></td>
  <td><div class="block">
  The list of vertices representing the polyline.
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
  <td><pre><code>GeoPolyline(GeoBox geoBox)</code></pre></td>
  <td><div class="block">
  Constructs an instance of this class from GeoBox .
  </div></td>
  </tr>
  <tr>
  <td><pre><code>GeoPolyline(List&lt;GeoCoordinates&gt; vertices)</code></pre></td>
  <td><div class="block">
  Constructs a GeoPolyline from the provided vertices.
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
  <td><a href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><pre><code>coordinatesAtOffsetInMeters(double offsetInMeters,
   GeoPolylineDirection direction)</code></pre></td>
  <td><div class="block">
  Returns the coordinates at the given distance along the polyline.
  </div></td>
  </tr>
  <tr>
  <td><code>boolean</code></td>
  <td><pre><code>equals(Object obj)</code></pre></td>
  <td> </td>
  </tr>
  <tr>
  <td><code>long</code></td>
  <td><pre><code>getNearestIndexTo(GeoCoordinates point)</code></pre></td>
  <td><div class="block">
  Returns the index of the nearest vertex to the given point.
  </div></td>
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

  - <div id="vertices" class="section detail">

    ### vertices

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")></span> <span class="element-name">vertices</span>

    </div>

    <div class="block">

    The list of vertices representing the polyline.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.util.List)" class="section detail">

    ### GeoPolyline

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolyline</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> vertices)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Constructs a GeoPolyline from the provided vertices. Throws an
    InstantiationError if the number of vertices is less than two.

    </div>

    Parameters:  
    `vertices` -

    List of vertices representing the polyline.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Instantiation error.

    </div>

  - <div id="<init>(com.here.sdk.core.GeoBox)" class="section detail">

    ### GeoPolyline

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolyline</span><span class="parameters">(@NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") geoBox)</span>

    </div>

    <div class="block">

    Constructs an instance of this class from GeoBox .

    </div>

    Parameters:  
    `geoBox` -

    A rectangle defined by the
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    to be converted into
    [`GeoPolyline`](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core").
    The corner coordinates of the
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    will define the points of the resulting
    [`GeoPolyline`](sdk-for-android-explore-com-here-sdk-core-geopolyline "class in com.here.sdk.core").

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

  - <div id="getNearestIndexTo(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### getNearestIndexTo

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">long</span> <span class="element-name">getNearestIndexTo</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") point)</span>

    </div>

    <div class="block">

    Returns the index of the nearest vertex to the given point.

    </div>

    Parameters:  
    `point` -

    Coordinates of the point.

    Returns:  
    Index of the closest vertex of the polyline.

    </div>

  - <div id="coordinatesAtOffsetInMeters(double,com.here.sdk.core.GeoPolylineDirection)"
    class="section detail">

    ### coordinatesAtOffsetInMeters

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">coordinatesAtOffsetInMeters</span><span class="parameters">(double offsetInMeters,
    @NonNull
    [GeoPolylineDirection](sdk-for-android-explore-com-here-sdk-core-geopolylinedirection "enum class in com.here.sdk.core") direction)</span>

    </div>

    <div class="block">

    Returns the coordinates at the given distance along the polyline.
    When the polyline is traversed from the beginning, the distance is
    calculated from the start of the polyline; while a direction from
    the end indicates a distance from the last vertex. The offset is
    expected to be non-negative and smaller than the length of the
    polyline. When the offset is negative, the function returns the
    starting end point of the polyline, i.e. the first vertex in
    positive direction and the last vertex in the negative direction.
    Similarly, when the offset is larger than the length of the
    polyline, then the function returns the opposite end point of the
    polyline. The distance between two consecutive vertices is
    calculated using the
    GeoCoordinates.distanceTo(com.here.sdk.core.GeoCoordinates)
    function. Therefore, it computes the distance (in meters) along the
    great circle between the two vertices. Similarly, the full length of
    the polyline is the sum of the distances between its vertices. The
    interpolation coordinates between two vertices is calculated using
    the GeoCoordinates.interpolate(com.here.sdk.core.GeoCoordinates,
    double) function. Note: the result may different from the analogue
    result from other matching components since they may adapt the
    result to the length of the underlying object described by the
    polyline.

    </div>

    Parameters:  
    `offsetInMeters` -

    The distance along the polyline in meters

    `direction` -

    The direction in which the polyline is traversed.

    Returns:  
    The coordinates of the point at the given distance

    </div>

  </div>

</div>


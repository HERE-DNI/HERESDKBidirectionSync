---
title: "CategoryQuery.Area (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-search-categoryquery-area"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.search](sdk-for-android-explore-com-here-sdk-search-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.search.CategoryQuery.Area

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[CategoryQuery](sdk-for-android-explore-com-here-sdk-search-categoryquery "class in com.here.sdk.search")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">CategoryQuery.Area</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Area to perform search on.

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
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area#areaCenter"
  class="member-name-link"><code>areaCenter</code></a></td>
  <td><div class="block">
  Geographic coordinates of the center around which to provide the most
  relevant places.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geobox"
  title="class in com.here.sdk.core"><code>GeoBox</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area#boxArea"
  class="member-name-link"><code>boxArea</code></a></td>
  <td><div class="block">
  Geographic rectangle area in which to provide the most relevant places.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocircle"
  title="class in com.here.sdk.core"><code>GeoCircle</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area#circleArea"
  class="member-name-link"><code>circleArea</code></a></td>
  <td><div class="block">
  Geographic circle area in which to provide the most relevant places.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocorridor"
  title="class in com.here.sdk.core"><code>GeoCorridor</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-search-categoryquery-area#corridorArea"
  class="member-name-link"><code>corridorArea</code></a></td>
  <td><div class="block">
  Geographic corridor area in which to provide the most relevant places.
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
  <td><pre><code>Area(GeoCoordinates areaCenter)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>Area(GeoCoordinates areaCenter,
   GeoBox boxArea)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>Area(GeoCoordinates areaCenter,
   GeoCircle circleArea)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>Area(GeoCorridor corridorArea,
   GeoCoordinates areaCenter)</code></pre></td>
  <td><div class="block">
  Constructs a new instance of this class from provided parameters.
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

  - <div id="areaCenter" class="section detail">

    ### areaCenter

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type">[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")</span> <span class="element-name">areaCenter</span>

    </div>

    <div class="block">

    Geographic coordinates of the center around which to provide the
    most relevant places.

    </div>

    </div>

  - <div id="boxArea" class="section detail">

    ### boxArea

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    final</span> <span class="return-type">[GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")</span> <span class="element-name">boxArea</span>

    </div>

    <div class="block">

    Geographic rectangle area in which to provide the most relevant
    places.

    </div>

    </div>

  - <div id="circleArea" class="section detail">

    ### circleArea

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    final</span> <span class="return-type">[GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core")</span> <span class="element-name">circleArea</span>

    </div>

    <div class="block">

    Geographic circle area in which to provide the most relevant places.

    </div>

    </div>

  - <div id="corridorArea" class="section detail">

    ### corridorArea

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public
    final</span> <span class="return-type">[GeoCorridor](sdk-for-android-explore-com-here-sdk-core-geocorridor "class in com.here.sdk.core")</span> <span class="element-name">corridorArea</span>

    </div>

    <div class="block">

    Geographic corridor area in which to provide the most relevant
    places. The contained polyline and half-width define the area that
    will be used in a search query. When used with SearchEngine , the
    polyline is compressed and sent. More complex polylines with large
    amounts of coordinates and with smaller half-width may have the less
    relevant part removed, such as the one far away from the search
    center. This usually makes no difference, because there will be
    enough POIs near the search center. For use cases where it is
    important to search the entire polyline, half-width can be increased
    or not set. For example: Route between New York and Chicago with
    half-width 800 will be added to request without removing the far
    away part, but route of the same length (around 360km) between Milan
    (Italy) and Konstanz (Germany) will have the far away part removed
    due to its complexity. When corridorArea is provided, areaCenter has
    to be within it, otherwise areaCenter is ignored when searching.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") areaCenter)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `areaCenter` -

    Geographic coordinates of the center around which to provide the
    most relevant places.

    </div>

  - <div id="<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoBox)"
    class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") areaCenter,
    @NonNull
    [GeoBox](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core") boxArea)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `areaCenter` -

    Geographic coordinates of the center around which to provide the
    most relevant places.

    `boxArea` -

    Geographic rectangle area in which to provide the most relevant
    places.

    </div>

  - <div id="<init>(com.here.sdk.core.GeoCoordinates,com.here.sdk.core.GeoCircle)"
    class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><span class="parameters">(@NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") areaCenter,
    @NonNull
    [GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core") circleArea)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.

    </div>

    Parameters:  
    `areaCenter` -

    Geographic coordinates of the center around which to provide the
    most relevant places.

    `circleArea` -

    Geographic circle area in which to provide the most relevant places.

    </div>

  - <div id="<init>(com.here.sdk.core.GeoCorridor,com.here.sdk.core.GeoCoordinates)"
    class="section detail">

    ### Area

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">Area</span><span class="parameters">(@NonNull
    [GeoCorridor](sdk-for-android-explore-com-here-sdk-core-geocorridor "class in com.here.sdk.core") corridorArea,
    @NonNull
    [GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core") areaCenter)</span>

    </div>

    <div class="block">

    Constructs a new instance of this class from provided parameters.
    The given corridor and center define the area that will be used in
    the search query. When used with SearchEngine , the polyline is
    compressed and sent. More complex polylines with large amounts of
    coordinates and with smaller half-width may have the less relevant
    part removed, such as the one far away from the search center. This
    usually makes no difference, because there will be enough POIs near
    the search center. For use cases where it is important to search the
    entire polyline, half-width can be increased or not set. For
    example: Route between New York and Chicago with half-width 800 will
    be added to request without removing the far away part, but route of
    the same length (around 360km) between Milan (Italy) and Konstanz
    (Germany) will have the far away part removed due to its complexity.
    The area center has to be within the corridor, otherwise it is
    ignored.

    </div>

    Parameters:  
    `corridorArea` -

    Geographic corridor area in which to provide the most relevant
    places.

    `areaCenter` -

    Geographic coordinates of the prioritized area center.

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


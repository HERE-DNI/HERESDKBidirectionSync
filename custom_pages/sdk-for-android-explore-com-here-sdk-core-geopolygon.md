---
title: "GeoPolygon (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-core-geopolygon"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.core](sdk-for-android-explore-com-here-sdk-core-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.core.GeoPolygon

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">GeoPolygon</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a GeoPolygon area as a series of geographic coordinates, and
optionally, a list of inner boundaries (also known as holes). An
instance of this class, initialized with appropriate vertices.

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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a><code>&gt;&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geopolygon#innerBoundaries"
  class="member-name-link"><code>innerBoundaries</code></a></td>
  <td><div class="block">
  The list of polygon inner boundaries (holes), each defined as a list of
  geographic coordinates.
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
  class="external-link"
  title="class or interface in java.util"><code>List</code></a><code>&lt;</code><a
  href="sdk-for-android-explore-com-here-sdk-core-geocoordinates"
  title="class in com.here.sdk.core"><code>GeoCoordinates</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-core-geopolygon#vertices"
  class="member-name-link"><code>vertices</code></a></td>
  <td><div class="block">
  The list of geographic coordinates representing the outer boundary
  vertices of polygon.
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
  <td><pre><code>GeoPolygon(GeoBox geoBox)</code></pre></td>
  <td><div class="block">
  Constructs an instance of this class from GeoBox .
  </div></td>
  </tr>
  <tr>
  <td><pre><code>GeoPolygon(GeoCircle geoCircle)</code></pre></td>
  <td><div class="block">
  Constructs an instance of this class from GeoCircle .
  </div></td>
  </tr>
  <tr>
  <td><pre><code>GeoPolygon(List&lt;GeoCoordinates&gt; vertices)</code></pre></td>
  <td><div class="block">
  Constructs an instance of this class from the provided vertices.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>GeoPolygon(List&lt;GeoCoordinates&gt; vertices,
   List&lt;List&lt;GeoCoordinates&gt;&gt; innerBoundaries)</code></pre></td>
  <td><div class="block">
  Constructs an instance of this class from the provided vertices and
  inner boundaries (holes).
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

    The list of geographic coordinates representing the outer boundary
    vertices of polygon.

    </div>

    </div>

  - <div id="innerBoundaries" class="section detail">

    ### innerBoundaries

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")>></span> <span class="element-name">innerBoundaries</span>

    </div>

    <div class="block">

    The list of polygon inner boundaries (holes), each defined as a list
    of geographic coordinates.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(java.util.List)" class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> vertices)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Constructs an instance of this class from the provided vertices.
    Throws InstantiationError if the number of vertices is less than
    three.

    </div>

    Parameters:  
    `vertices` -

    List of vertices representing the polygon outer boundary in
    clockwise order.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Instantiation error.

    </div>

  - <div id="<init>(java.util.List,java.util.List)"
    class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")> vertices,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html"
    class="external-link" title="class or interface in java.util">List</a><[GeoCoordinates](sdk-for-android-explore-com-here-sdk-core-geocoordinates "class in com.here.sdk.core")>> innerBoundaries)</span>
    throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Constructs an instance of this class from the provided vertices and
    inner boundaries (holes). Throws InstantiationError if the number of
    vertices is less than three.

    </div>

    Parameters:  
    `vertices` -

    List of vertices representing the polygon outer boundary in
    clockwise order.

    `innerBoundaries` -

    List of polygon inner boundaries (holes), each in counterclockwise
    order.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")
    -

    Instantiation error.

    </div>

  - <div id="<init>(com.here.sdk.core.GeoCircle)"
    class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
    [GeoCircle](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core") geoCircle)</span>

    </div>

    <div class="block">

    Constructs an instance of this class from GeoCircle .

    </div>

    Parameters:  
    `geoCircle` -

    A
    [`GeoCircle`](sdk-for-android-explore-com-here-sdk-core-geocircle "class in com.here.sdk.core")
    to be converted into
    [`GeoPolygon`](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core").

    </div>

  - <div id="<init>(com.here.sdk.core.GeoBox)" class="section detail">

    ### GeoPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GeoPolygon</span><span class="parameters">(@NonNull
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
    [`GeoPolygon`](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core").
    The corner coordinates defined by the
    [`GeoBox`](sdk-for-android-explore-com-here-sdk-core-geobox "class in com.here.sdk.core")
    will define the outer boundary verticies of the
    [`GeoPolygon`](sdk-for-android-explore-com-here-sdk-core-geopolygon "class in com.here.sdk.core").

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


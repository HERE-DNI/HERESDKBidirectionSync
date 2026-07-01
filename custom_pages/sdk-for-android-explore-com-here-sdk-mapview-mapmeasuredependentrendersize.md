---
title: "MapMeasureDependentRenderSize (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapMeasureDependentRenderSize

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapMeasureDependentRenderSize</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents a render size, described as map measure dependent values.

</div>

</div>

<div class="section summary">

- <div id="nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

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
  <th>Class</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><code>static enum </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize.InstantiationErrorCode</code></a></td>
  <td><div class="block">
  Describes a reason for failing to create a MapMeasureDependentRenderSize
  .
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize.InstantiationException</code></a></td>
  <td><div class="block">
  Thrown when a problem occurs while trying to create
  MapMeasureDependentRenderSize .
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

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
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasure-kind"
  title="enum class in com.here.sdk.mapview"><code>MapMeasure.Kind</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize#measureKind"
  class="member-name-link"><code>measureKind</code></a></td>
  <td><div class="block">
  The unit used for the key in sizes .
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a><code>&lt;</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a><code>,</code><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a><code>&gt;</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes"
  class="member-name-link"><code>sizes</code></a></td>
  <td><div class="block">
  The dictionary describing the size (value) per map measure (key).
  </div></td>
  </tr>
  <tr>
  <td><code>final </code><a
  href="sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit"
  title="enum class in com.here.sdk.mapview"><code>RenderSize.Unit</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize#sizeUnit"
  class="member-name-link"><code>sizeUnit</code></a></td>
  <td><div class="block">
  The unit used for the value in sizes .
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
  <td><pre><code>MapMeasureDependentRenderSize(MapMeasure.Kind measureKind,
   RenderSize.Unit sizeUnit,
   Map&lt;Double,Double&gt; sizes)</code></pre></td>
  <td><div class="block">
  Constructs a MapMeasureDependentRenderSize from given parameters.
  </div></td>
  </tr>
  <tr>
  <td><pre><code>MapMeasureDependentRenderSize(RenderSize.Unit sizeUnit,
   double size)</code></pre></td>
  <td><div class="block">
  Constructs a MapMeasureDependentRenderSize from single size value which
  is constant across all map measures.
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

  - <div id="measureKind" class="section detail">

    ### measureKind

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type">[MapMeasure.Kind](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure-kind "enum class in com.here.sdk.mapview")</span> <span class="element-name">measureKind</span>

    </div>

    <div class="block">

    The unit used for the key in sizes .

    </div>

    </div>

  - <div id="sizeUnit" class="section detail">

    ### sizeUnit

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type">[RenderSize.Unit](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview")</span> <span class="element-name">sizeUnit</span>

    </div>

    <div class="block">

    The unit used for the value in sizes .

    </div>

    </div>

  - <div id="sizes" class="section detail">

    ### sizes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>></span> <span class="element-name">sizes</span>

    </div>

    <div class="block">

    The dictionary describing the size (value) per map measure (key).
    Units of keys and values are defined in measureKind and sizeUnit .
    sizes with a single entry indicates using a fixed size value across
    all map measures.

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>(com.here.sdk.mapview.MapMeasure.Kind,com.here.sdk.mapview.RenderSize.Unit,java.util.Map)"
    class="section detail">

    ### MapMeasureDependentRenderSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMeasureDependentRenderSize</span><span class="parameters">(@NonNull
    [MapMeasure.Kind](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure-kind "enum class in com.here.sdk.mapview") measureKind,
    @NonNull
    [RenderSize.Unit](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview") sizeUnit,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a><<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>,<a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
    class="external-link" title="class or interface in java.lang">Double</a>> sizes)</span>
    throws
    <span class="exceptions">[MapMeasureDependentRenderSize.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Constructs a MapMeasureDependentRenderSize from given parameters.
    Supplying sizes map with a single entry indicates using a fixed size
    value across all map measures.

    </div>

    Parameters:  
    `measureKind` -

    The unit used for the key in `sizes`.

    `sizeUnit` -

    The unit used for the value in `sizes`.

    `sizes` -

    The dictionary describing the size (value) per map measure (key).

    Throws:  
    [`MapMeasureDependentRenderSize.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")
    -

    Instantiation error if `sizes` map is empty or contains negative
    keys or values.

    </div>

  - <div id="<init>(com.here.sdk.mapview.RenderSize.Unit,double)"
    class="section detail">

    ### MapMeasureDependentRenderSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMeasureDependentRenderSize</span><span class="parameters">(@NonNull
    [RenderSize.Unit](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview") sizeUnit,
    double size)</span> throws
    <span class="exceptions">[MapMeasureDependentRenderSize.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Constructs a MapMeasureDependentRenderSize from single size value
    which is constant across all map measures. The given size value is
    stored in sizes map at key 0 and measureKind is set to
    MapMeasure.Kind.ZOOM_LEVEL .

    </div>

    Parameters:  
    `sizeUnit` -

    The unit used for the value in `size`.

    `size` -

    The size independent of map measure. Must not be negative.

    Throws:  
    [`MapMeasureDependentRenderSize.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception "class in com.here.sdk.mapview")
    -

    Instantiation error if `size` is negative.

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


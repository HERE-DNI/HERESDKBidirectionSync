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

<div id="sdk-for-android-explore-class-description"
class="section class-description">

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

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes a reason for failing to create a
  MapMeasureDependentRenderSize .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapMeasureDependentRenderSize.InstantiationException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Thrown when a problem occurs while trying to create
  MapMeasureDependentRenderSize .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-field-summary"
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

  `final `[`MapMeasure.Kind`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure-kind "enum class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize#measureKind"
  class="member-name-link"><code>measureKind</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The unit used for the key in sizes .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `final `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
  class="external-link"
  title="class or interface in java.util"><code>Map</code></a>`<`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>`,`<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Double.html"
  class="external-link"
  title="class or interface in java.lang"><code>Double</code></a>`>`

  </div>

  <div class="col-second odd-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize#sizes"
  class="member-name-link"><code>sizes</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  The dictionary describing the size (value) per map measure (key).

  </div>

  </div>

  <div class="col-first even-row-color">

  `final `[`RenderSize.Unit`](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color">

  <a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize#sizeUnit"
  class="member-name-link"><code>sizeUnit</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  The unit used for the value in sizes .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-constructor-summary"
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

      MapMeasureDependentRenderSize(MapMeasure.Kind measureKind,
       RenderSize.Unit sizeUnit,
       Map<Double,Double> sizes)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Constructs a MapMeasureDependentRenderSize from given parameters.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapMeasureDependentRenderSize(RenderSize.Unit sizeUnit,
       double size)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Constructs a MapMeasureDependentRenderSize from single size value
  which is constant across all map measures.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
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

- <div id="sdk-for-android-explore-field-detail"
  class="section field-details">

  - <div id="sdk-for-android-explore-measureKind"
    class="section detail">

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

  - <div id="sdk-for-android-explore-sizeUnit" class="section detail">

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

  - <div id="sdk-for-android-explore-sizes" class="section detail">

    ### sizes

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public
    final</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
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

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapMeasure.Kind,com.here.sdk.mapview.RenderSize.Unit,java.util.Map)"
    class="section detail">

    ### MapMeasureDependentRenderSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapMeasureDependentRenderSize</span><span class="parameters">(@NonNull
    [MapMeasure.Kind](sdk-for-android-explore-com-here-sdk-mapview-mapmeasure-kind "enum class in com.here.sdk.mapview") measureKind,
    @NonNull
    [RenderSize.Unit](sdk-for-android-explore-com-here-sdk-mapview-rendersize-unit "enum class in com.here.sdk.mapview") sizeUnit,
    @NonNull <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html"
    class="external-link" title="class or interface in java.util">Map</a>\<<a
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

    Instantiation error if `sizes` map is empty or contains negative
    keys or values.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.RenderSize.Unit,double)"
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

    Instantiation error if `size` is negative.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-equals(java.lang.Object)"
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

  - <div id="sdk-for-android-explore-hashCode()" class="section detail">

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


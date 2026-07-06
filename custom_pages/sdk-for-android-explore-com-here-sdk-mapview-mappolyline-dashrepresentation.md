---
title: "MapPolyline.DashRepresentation (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mappolyline-dashrepresentation"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapItemRepresentationcom.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.DashRepresentation
→ com.here.NativeBase →
com.here.sdk.mapview.MapItemRepresentationcom.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.DashRepresentation
→ com.here.sdk.mapview.MapItemRepresentation →
com.here.sdk.mapview.MapPolyline.Representationcom.here.sdk.mapview.MapPolyline.DashRepresentation
→ com.here.sdk.mapview.MapPolyline.Representation →
com.here.sdk.mapview.MapPolyline.DashRepresentation

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

Enclosing class:  
[MapPolyline](sdk-for-android-explore-com-here-sdk-mapview-mappolyline "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapPolyline.DashRepresentation</span>
<span class="extends-implements">extends
[MapPolyline.Representation](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation "class in com.here.sdk.mapview")</span>

</div>

<div class="block">

Represents a dash pattern for map polyline where the dash can be
rendered as a colored line and the gap can be either empty or colored.
The length of the dash and gap are set independently, allowing for
patterns like ' — — — —' (dash length = gap length) or ' ——— ——— ———'
(dash length != gap length).

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-nested-class-summary"
  class="section nested-class-summary">

  <div class="inherited-list">

  [`MapPolyline.Representation.InstantiationErrorCode`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationerrorcode "enum class in com.here.sdk.mapview"), [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

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

      DashRepresentation(MapMeasureDependentRenderSize lineWidth,
       MapMeasureDependentRenderSize dashLength,
       MapMeasureDependentRenderSize gapLength,
       Color dashColor)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a representation for a dashed line.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      DashRepresentation(MapMeasureDependentRenderSize lineWidth,
       MapMeasureDependentRenderSize dashLength,
       MapMeasureDependentRenderSize gapLength,
       Color dashColor,
       Color gapColor)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a representation for a dashed line with both dash and the gap
  being colored.

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

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDashColor()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the color of the dashes of the polyline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDashLength()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent polyline dash length.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`Color`](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGapColor()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the color for the gaps of the polyline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGapLength()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent polyline gap length.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  [`MapMeasureDependentRenderSize`](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getLineWidth()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the map measure dependent polyline width.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color)"
    class="section detail">

    ### DashRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DashRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") gapLength,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") dashColor)</span>
    throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a representation for a dashed line. Gaps are not displayed.
    At map measures smaller than the smallest map measure in the
    lineWidth , dashLength and gapLength , the value used for rendering
    is constant and equal to the value given for the smallest map
    measure in the respective MapMeasureDependentRenderSize object. At
    map measures bigger than the biggest map measure in the lineWidth ,
    dashLength and gapLength , the value used for rendering is constant
    and equal to the value given for the biggest map measure in the
    respective MapMeasureDependentRenderSize object. At map measures
    between two nearest given map measures, the values are linearly
    interpolated between values given for these map measures. For
    MapMeasure.Kind only MapMeasure.Kind.ZOOM_LEVEL is supported. For
    RenderSize.Unit only RenderSize.Unit.PIXELS is supported. All sizes
    must not be 0 ( MapMeasureDependentRenderSize.sizes with all values
    set to 0.0).

    </div>

    Parameters:  
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `dashLength` -

    The dash length of the polyline depending on the map measure.

    `gapLength` -

    The gap length of the polyline depending on the map measure.

    `dashColor` -

    The dash color of the polyline.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  - <div id="sdk-for-android-explore-<init>(com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.mapview.MapMeasureDependentRenderSize,com.here.sdk.core.Color,com.here.sdk.core.Color)"
    class="section detail">

    ### DashRepresentation

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">DashRepresentation</span><span class="parameters">(@NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") lineWidth,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") dashLength,
    @NonNull
    [MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview") gapLength,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") dashColor,
    @NonNull
    [Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core") gapColor)</span>
    throws
    <span class="exceptions">[MapPolyline.Representation.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates a representation for a dashed line with both dash and the
    gap being colored. At map measures smaller than the smallest map
    measure in the lineWidth , dashLength and gapLength , the value used
    for rendering is constant and equal to the value given for the
    smallest map measure in the respective MapMeasureDependentRenderSize
    object. At map measures bigger than the biggest map measure in the
    lineWidth , dashLength and gapLength , the value used for rendering
    is constant and equal to the value given for the biggest map measure
    in the respective MapMeasureDependentRenderSize object. At map
    measures between two nearest given map measures, the values are
    linearly interpolated between values given for these map measures.
    For MapMeasure.Kind only MapMeasure.Kind.ZOOM_LEVEL is supported.
    For RenderSize.Unit only RenderSize.Unit.PIXELS is supported. All
    sizes must not be 0 ( MapMeasureDependentRenderSize.sizes with all
    values set to 0.0).

    </div>

    Parameters:  
    `lineWidth` -

    The width of the polyline depending on the map measure.

    `dashLength` -

    The dash length of the polyline depending on the map measure.

    `gapLength` -

    The gap length of the polyline depending on the map measure.

    `dashColor` -

    The color of the dashes.

    `gapColor` -

    The color of the gaps.

    Throws:  
    [`MapPolyline.Representation.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-mappolyline-representation-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-getLineWidth()"
    class="section detail">

    ### getLineWidth

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getLineWidth</span>()

    </div>

    <div class="block">

    Gets the map measure dependent polyline width. At map measures
    smaller than smallest map measure in the lineWidth line width is
    constant and equal to the width given for the smallest map measure
    in the lineWidth . At map measures bigger than biggest map measure
    in the lineWidth line width is constant and equal to the width given
    for the biggest map measure in the lineWidth . At map measures
    between two nearest given map measures, the values are linearly
    interpolated between values given for these map measures.

    </div>

    Returns:  
    The width of the polyline depending on the map measure.

    </div>

  - <div id="sdk-for-android-explore-getDashLength()"
    class="section detail">

    ### getDashLength

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getDashLength</span>()

    </div>

    <div class="block">

    Gets the map measure dependent polyline dash length. At map measures
    smaller than smallest map measure in the dashLength line width is
    constant and equal to the width given for the smallest map measure
    in the dashLength . At map measures bigger than biggest map measure
    in the dashLength line width is constant and equal to the width
    given for the biggest map measure in the dashLength . At map
    measures between two nearest given map measures, the values are
    linearly interpolated between values given for these map measures.

    </div>

    Returns:  
    The dash length of the polyline depending on the map measure.

    </div>

  - <div id="sdk-for-android-explore-getGapLength()"
    class="section detail">

    ### getGapLength

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapMeasureDependentRenderSize](sdk-for-android-explore-com-here-sdk-mapview-mapmeasuredependentrendersize "class in com.here.sdk.mapview")</span> <span class="element-name">getGapLength</span>()

    </div>

    <div class="block">

    Gets the map measure dependent polyline gap length. At map measures
    smaller than smallest map measure in the gapLength line width is
    constant and equal to the width given for the smallest map measure
    in the gapLength . At map measures bigger than biggest map measure
    in the gapLength line width is constant and equal to the width given
    for the biggest map measure in the gapLength . At map measures
    between two nearest given map measures, the values are linearly
    interpolated between values given for these map measures.

    </div>

    Returns:  
    The gap length of the polyline depending on the map measure.

    </div>

  - <div id="sdk-for-android-explore-getDashColor()"
    class="section detail">

    ### getDashColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getDashColor</span>()

    </div>

    <div class="block">

    Gets the color of the dashes of the polyline.

    </div>

    Returns:  
    The color of the dashes of the polyline.

    </div>

  - <div id="sdk-for-android-explore-getGapColor()"
    class="section detail">

    ### getGapColor

    <div class="member-signature">

    <span class="annotations">@Nullable
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">getGapColor</span>()

    </div>

    <div class="block">

    Gets the color for the gaps of the polyline. Returns null if no
    color is used.

    </div>

    Returns:  
    The color for the gaps of the polyline. The default value is `null`
    and no color is used.

    </div>

  </div>

</div>


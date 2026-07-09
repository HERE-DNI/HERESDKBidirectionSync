---
title: "MapPolygon (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolygon"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapPolygon → com.here.NativeBase com.here.sdk.mapview.MapPolygon → com.here.sdk.mapview.MapPolygon

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapPolygon</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

A visual representation of a polygon on the map. Can be used to visualize areas of all shapes and sizes. The geometry to be visualized is represented by an instance of GeoPolygon . To display circular areas (for example, a position accuracy indicator) use a GeoPolygon created from a GeoCircle using GeoPolygon(GeoCircle) . Note: The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur. Polygons which are self-intersecting are not supported and may lead to render artifacts. The inner boundaries (holes) specified in the GeoPolygon are ignored.

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

      MapPolygon ( GeoPolygon geometry, Color color)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapPolygon ( GeoPolygon geometry, Color color, Color outlineColor,
       double outlineWidthInPixels)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in.

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

  `int`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getDrawOrder ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the draw order of this map polygon relative to other map polygons.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">`Color`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getFillColor ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current color of the fill.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">`GeoPolygon`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getGeometry ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the current geometry of the polygon.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">`Metadata`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getMetadata ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the Metadata instance attached to this polygon.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">`Color`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOutlineColor ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the color of the polygon outline.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `double`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getOutlineWidth ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the outline width of the polygon in pixels.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">`MapMeasureRange`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getVisibilityRanges ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the list of visibility ranges.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setDrawOrder (int value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the draw order of this map polygon relative to other map polygons.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setFillColor ( Color value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the current color of the fill.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setGeometry ( GeoPolygon value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets a new geometry to update the appearance.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setMetadata ( Metadata value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the Metadata instance to be attached to this polygon.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOutlineColor ( Color value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the color of the polygon outline.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setOutlineWidth (double value)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the outline width of the polygon in pixels.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setVisibilityRanges ( List < MapMeasureRange > value)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets visibility ranges for this map polygon.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoPolygon-com-here-sdk-core-Color" class="section detail">

    ### MapPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapPolygon</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color)</span>

    </div>

    <div class="block">

    Creates a new MapPolygon instance with outline visualization disabled and containing the geometry passed in. The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed. Note: The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur. Polygons which are self-intersecting are not supported and may lead to render artifacts. The inner boundaries (holes) specified in the GeoPolygon are ignored.

    </div>

    Parameters:  
    `geometry` -

    The list of vertices representing the outer boundary of polygon.

    `color` -

    The fill color for the polygon

    </div>

  - <div id="sdk-for-android-navigate-init-com-here-sdk-core-GeoPolygon-com-here-sdk-core-Color-com-here-sdk-core-Color-double" class="section detail">

    ### MapPolygon

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapPolygon</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> geometry, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> color, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> outlineColor, double outlineWidthInPixels)</span>

    </div>

    <div class="block">

    Creates a new MapPolygon instance with outline visualization enabled and containing the geometry passed in. Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque by interpreting the alpha value as 1. The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed. Note: The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur. Polygons which are self-intersecting are not supported and may lead to render artifacts. The inner boundaries (holes) specified in the GeoPolygon are ignored.

    </div>

    Parameters:  
    `geometry` -

    The list of vertices representing the outer boundary of polygon.

    `color` -

    The fill color for the polygon.

    `outlineColor` -

    The color of the polygon outline, alpha channel is ignored and treated as 1.

    `outlineWidthInPixels` -

    The width of the polygon outline (in pixels). Negative values are clamped to 0.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-getGeometry" class="section detail">

    ### getGeometry

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a></span> <span class="element-name">getGeometry</span>()

    </div>

    <div class="block">

    Gets the current geometry of the polygon.

    </div>

    Returns:  
    The geometry of the polygon. Setting a new geometry will update the appearance.

    </div>

  - <div id="sdk-for-android-navigate-setGeometry-com-here-sdk-core-GeoPolygon" class="section detail">

    ### setGeometry

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setGeometry</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-geopolygon" title="class in com.here.sdk.core">GeoPolygon</a> value)</span>

    </div>

    <div class="block">

    Sets a new geometry to update the appearance. The winding order of the vertices can be in clockwise or counter-clockwise order. It is recomended to provide the outer boundary ordered clockwise and closed. Note: The polygon shape should not cover more than half of the globe, otherwise unexpected results may occur. Polygons which are self-intersecting are not supported and may lead to render artifacts. The inner boundaries (holes) specified in the GeoPolygon are ignored.

    </div>

    Parameters:  
    `value` -

    The geometry of the polygon. Setting a new geometry will update the appearance.

    </div>

  - <div id="sdk-for-android-navigate-getMetadata" class="section detail">

    ### getMetadata

    <div class="member-signature">

    <span class="annotations">@Nullable </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a></span> <span class="element-name">getMetadata</span>()

    </div>

    <div class="block">

    Gets the Metadata instance attached to this polygon.

    </div>

    Returns:  
    The Metadata instance attached to this polygon, `null` by default.

    </div>

  - <div id="sdk-for-android-navigate-setMetadata-com-here-sdk-core-Metadata" class="section detail">

    ### setMetadata

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setMetadata</span><wbr></wbr><span class="parameters">(@Nullable <a href="sdk-for-android-navigate-com-here-sdk-core-metadata" title="class in com.here.sdk.core">Metadata</a> value)</span>

    </div>

    <div class="block">

    Sets the Metadata instance to be attached to this polygon.

    </div>

    Parameters:  
    `value` -

    The Metadata instance attached to this polygon, `null` by default.

    </div>

  - <div id="sdk-for-android-navigate-getFillColor" class="section detail">

    ### getFillColor

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a></span> <span class="element-name">getFillColor</span>()

    </div>

    <div class="block">

    Gets the current color of the fill.

    </div>

    Returns:  
    Color of the polygon's fill.

    </div>

  - <div id="sdk-for-android-navigate-setFillColor-com-here-sdk-core-Color" class="section detail">

    ### setFillColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setFillColor</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span>

    </div>

    <div class="block">

    Sets the current color of the fill. Fully transparent color (alpha set to 0) disables the fill completely.

    </div>

    Parameters:  
    `value` -

    Color of the polygon's fill.

    </div>

  - <div id="sdk-for-android-navigate-getDrawOrder" class="section detail">

    ### getDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">getDrawOrder</span>()

    </div>

    <div class="block">

    Gets the draw order of this map polygon relative to other map polygons. Default value is 0.

    </div>

    Returns:  
    The draw order of this map polygon relative to other map polygons.

    </div>

  - <div id="sdk-for-android-navigate-setDrawOrder-int" class="section detail">

    ### setDrawOrder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setDrawOrder</span><wbr></wbr><span class="parameters">(int value)</span>

    </div>

    <div class="block">

    Sets the draw order of this map polygon relative to other map polygons. Polygon with higher draw order value are drawn on top of polygons with lower draw order. In case multiple polygons have the same draw order value then the order in which they were added to the scene matters. Last added polygon is drawn on top. Allowed range is 0-1023. Values outside this range will be clamped.

    </div>

    Parameters:  
    `value` -

    The draw order of this map polygon relative to other map polygons.

    </div>

  - <div id="sdk-for-android-navigate-getVisibilityRanges" class="section detail">

    ### getVisibilityRanges

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>\></span> <span class="element-name">getVisibilityRanges</span>()

    </div>

    <div class="block">

    Gets the list of visibility ranges. The map polygon is visible only inside these map measure ranges. When empty (the default), the map polygon is visible without map measure restrictions.

    </div>

    Returns:  
    The list of visibility ranges. The map polygon is visible only inside these map measure ranges.

    </div>

  - <div id="sdk-for-android-navigate-setVisibilityRanges-java-util-List" class="section detail">

    ### setVisibilityRanges

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setVisibilityRanges</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-mapview-mapmeasurerange" title="class in com.here.sdk.mapview">MapMeasureRange</a>\> value)</span>

    </div>

    <div class="block">

    Sets visibility ranges for this map polygon. A range is half open - \<a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">minimumZoomLevel, maximumZoomLevel), the given maximum value is not contained in the range. The map polygon is visible only inside these map measure ranges. When empty (the default), the map polygon is visible without map measure restrictions. Only MapMeasureRange (s) of MapMeasure.Kind.ZOOM_LEVEL type are supported. MapMeasureRange (s) of other unsupported types will be ignored.

    </div>

    Parameters:  
    `value` -

    The list of visibility ranges. The map polygon is visible only inside these map measure ranges.

    </div>

  - <div id="sdk-for-android-navigate-getOutlineColor" class="section detail">

    ### getOutlineColor

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type">[Color</a></span> <span class="element-name">getOutlineColor</span>()

    </div>

    <div class="block">

    Gets the color of the polygon outline. The default outline color is opaque white.

    </div>

    Returns:  
    The color of the polygon outline.

    </div>

  - <div id="sdk-for-android-navigate-setOutlineColor-com-here-sdk-core-Color" class="section detail">

    ### setOutlineColor

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOutlineColor</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-core-color" title="class in com.here.sdk.core">Color</a> value)</span>

    </div>

    <div class="block">

    Sets the color of the polygon outline. Transparent outlines are not supported. Any color with transparency (alpha value other than 1) will be rendered as fully opaque.

    </div>

    Parameters:  
    `value` -

    The color of the polygon outline.

    </div>

  - <div id="sdk-for-android-navigate-getOutlineWidth" class="section detail">

    ### getOutlineWidth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">getOutlineWidth</span>()

    </div>

    <div class="block">

    Gets the outline width of the polygon in pixels. By default, the outline width is set to zero.

    </div>

    Returns:  
    The width of the polygon outline in pixels.

    </div>

  - <div id="sdk-for-android-navigate-setOutlineWidth-double" class="section detail">

    ### setOutlineWidth

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setOutlineWidth</span><wbr></wbr><span class="parameters">(double value)</span>

    </div>

    <div class="block">

    Sets the outline width of the polygon in pixels. The value should be greater than or equal to 0. Negative values are clamped to zero.

    </div>

    Parameters:  
    `value` -

    The width of the polygon outline in pixels.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


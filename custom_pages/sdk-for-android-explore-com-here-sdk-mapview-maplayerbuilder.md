---
title: "MapLayerBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.MapLayerBuilder →
com.here.NativeBase → com.here.sdk.mapview.MapLayerBuilder

</div>

<div id="class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapLayerBuilder</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

MapLayerBuilder is used to add layers to a map to visualise a dataset in
a programmatic way without defining it upfront in the configuration
files. For example, after loading a scene configuration file, the
renderer is setup to draw layers in the following order: background
water roads:outline roads labels Rendering order of elements in a single
map layer can be controlled with categories. Layer names are unique, and
category names have to be unique within a layer. The layer's default,
main category is unnamed. The concept of 'category' is tightly linked to
styling. The idea behind category is that one should be able to style
separately elements in a map layer. Take, for instance, roads. If one
wants to style separately the bridges it will create a category
'bridges' and style it accordingly in the style file. If the user does
not intend to or cannot style elements of the layer differently then it
should opt for a layer with only the default category (e.g. for a raster
layer, only the default category makes sense, since the layer has no
other stylable elements apart from the raster image). A new layer called
'zone' and its category 'background' can be added dynamically so that
the rendering order gets modified in the following way: background water
zone:background zone roads:outline roads labels This could be achieved
with the help of the MapLayerPriorityBuilder and the MapLayerBuilder as
in the following example: MapLayerPriority layerPriority = new
MapLayerPriorityBuilder() .renderedAfterLayer("water") // places main
category after 'water' .withCategory("background")
.renderedAfterLayer("water") // places 'background' category after
'water' and before the // layer's main category. .build(); MapLayer
layer = new MapLayerBuilder() .withDataSource("DataSourceName",
MapContentType.LINE) .forMap(map) .withName("zone")
.withPriority(layerPriority) .build(); In case no layer priority or an
empty one is provided, or if a reference layer-category pair is not
present in the rendering order, the layer is going to be rendered last
with respect to the rendering order at the time of its creation. Due to
current limitations, the MapLayerPriority assignment is not implemented
for point map layers. All labels will be rendered within the "labels"
layer, defined in the scene configuration file. By default, all labels
rendered by a point map layer are rendered last and no overlapping is
allowed. The following categories can be used to have a different
behaviour: 'custom-labels' A label should be rendered first, is allowed
to overlap with other labels of the same category and block map labels.
'custom-labels-no-self-overlap' A label should be rendered after
'custom-labels', is not allowed to overlap with other labels of the same
categoty and block map labels. 'custom-labels-overlap-all' A label
should be rendered last, is allowed to overlap all predefined
categories, also map labels. These categories are configured accordingly
in the basic map scene configurations. Category assignment to features
can be done in the style based on data attributes. The category
assignment can be done for all types of content: point, line, polygon.

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
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationerrorcode"
  class="type-name-link"
  title="enum class in com.here.sdk.mapview"><code>MapLayerBuilder.InstantiationErrorCode</code></a></td>
  <td><div class="block">
  Describes a reason for failing to build a MapLayer .
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationerrordetails"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder.InstantiationErrorDetails</code></a></td>
  <td><div class="block">
  Describes the reason for failing to build a MapLayer .
  </div></td>
  </tr>
  <tr>
  <td><code>static final class </code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationexception"
  class="type-name-link"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder.InstantiationException</code></a></td>
  <td><div class="block">
  Thrown when failing to build a MapLayer .
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
  <td><pre><code>MapLayerBuilder()</code></pre></td>
  <td><div class="block">
  Creates an instance of the layer builder interface.
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
  <td><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayer"
  title="class in com.here.sdk.mapview"><code>MapLayer</code></a></td>
  <td><pre><code>build()</code></pre></td>
  <td><div class="block">
  Constructs, registers and configures a new map layer showing specified
  content type according to the configured parameters.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>forMap(HereMap targetMap)</code></pre></td>
  <td><div class="block">
  Configures the builder to display a layer in the given map.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>withDataSource(String dataSourceName,
   MapContentType contentType)</code></pre></td>
  <td><div class="block">
  Configures the builder to use a data source with the given name as the
  source of data for the layer.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>withLoadPriority(double loadPriority)</code></pre></td>
  <td><div class="block">
  Configures the builder to set the layer load priority.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>withMapMeasureDependentStorageLevels(MapLayerMapMeasureDependentStorageLevels mapLayerMapMeasureDependentStorageLevels)</code></pre></td>
  <td><div class="block">
  Applies a mapping from the map measure to the storage level.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>withName(String name)</code></pre></td>
  <td><div class="block">
  Configures builder to use the given name as a layer name.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>withPriority(MapLayerPriority priority)</code></pre></td>
  <td><div class="block">
  Configures the builder to set the MapLayerPriority to be used by the
  layer.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>withStyle(Style style)</code></pre></td>
  <td><div class="block">
  Configures the builder to use a style.
  </div></td>
  </tr>
  <tr>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder"
  title="class in com.here.sdk.mapview"><code>MapLayerBuilder</code></a></td>
  <td><pre><code>withVisibilityRange(MapLayerVisibilityRange visibilityRange)</code></pre></td>
  <td><div class="block">
  Configures the builder to set the layer visible in the given zoom levels
  range.
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
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
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

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### MapLayerBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapLayerBuilder</span>()

    </div>

    <div class="block">

    Creates an instance of the layer builder interface.

    </div>

    </div>

  </div>

- <div id="method-detail" class="section method-details">

  - <div id="withName(java.lang.String)" class="section detail">

    ### withName

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withName</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> name)</span>

    </div>

    <div class="block">

    Configures builder to use the given name as a layer name. The name
    is a mandatory layer creation parameter.

    </div>

    Parameters:  
    `name` -

    Name of the layer. Must be unique.

    Returns:  
    This class instance.

    </div>

  - <div id="withDataSource(java.lang.String,com.here.sdk.mapview.MapContentType)"
    class="section detail">

    ### withDataSource

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withDataSource</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> dataSourceName,
    @NonNull
    [MapContentType](sdk-for-android-explore-com-here-sdk-mapview-mapcontenttype "enum class in com.here.sdk.mapview") contentType)</span>

    </div>

    <div class="block">

    Configures the builder to use a data source with the given name as
    the source of data for the layer. The datasource name and content
    type are mandatory layer creation parameters.

    </div>

    Parameters:  
    `dataSourceName` -

    Name of the data source.

    `contentType` -

    The renderable content type supplied by the data source.

    Returns:  
    This class instance.

    </div>

  - <div id="withStyle(com.here.sdk.mapview.Style)"
    class="section detail">

    ### withStyle

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withStyle</span><span class="parameters">(@NonNull
    [Style](sdk-for-android-explore-com-here-sdk-mapview-style "class in com.here.sdk.mapview") style)</span>

    </div>

    <div class="block">

    Configures the builder to use a style. Providing a style during
    layer creation is not mandatory. The style can also be set/updated
    after the layer creation. For more details see Custom Layer Style
    Reference in the documentation. Note: This is a beta release of this
    feature, so there could be a few bugs and unexpected behavior.
    Related APIs may change for new releases without a deprecation
    process.

    </div>

    Parameters:  
    `style` -

    Style for the layer.

    Returns:  
    This class instance.

    </div>

  - <div id="forMap(com.here.sdk.mapview.HereMap)"
    class="section detail">

    ### forMap

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">forMap</span><span class="parameters">(@NonNull
    [HereMap](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview") targetMap)</span>

    </div>

    <div class="block">

    Configures the builder to display a layer in the given map. The map
    is a mandatory layer creation parameter.

    </div>

    Parameters:  
    `targetMap` -

    The map.

    Returns:  
    This class instance.

    </div>

  - <div id="withPriority(com.here.sdk.mapview.MapLayerPriority)"
    class="section detail">

    ### withPriority

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withPriority</span><span class="parameters">(@NonNull
    [MapLayerPriority](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview") priority)</span>

    </div>

    <div class="block">

    Configures the builder to set the MapLayerPriority to be used by the
    layer.

    </div>

    Parameters:  
    `priority` -

    MapLayerPriority which should be applied to the layer.

    Returns:  
    This class instance.

    </div>

  - <div id="withVisibilityRange(com.here.sdk.mapview.MapLayerVisibilityRange)"
    class="section detail">

    ### withVisibilityRange

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withVisibilityRange</span><span class="parameters">(@NonNull
    [MapLayerVisibilityRange](sdk-for-android-explore-com-here-sdk-mapview-maplayervisibilityrange "class in com.here.sdk.mapview") visibilityRange)</span>

    </div>

    <div class="block">

    Configures the builder to set the layer visible in the given zoom
    levels range. Values outside the map zoom level range (0, 24) will
    be ignored. Providing the visibility range is optional. If not
    provided, the layer will be visible on all zoom levels.

    </div>

    Parameters:  
    `visibilityRange` -

    Visibility range which should be applied to the layer.

    Returns:  
    This class instance.

    </div>

  - <div id="withMapMeasureDependentStorageLevels(com.here.sdk.mapview.MapLayerMapMeasureDependentStorageLevels)"
    class="section detail">

    ### withMapMeasureDependentStorageLevels

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withMapMeasureDependentStorageLevels</span><span class="parameters">(@NonNull
    [MapLayerMapMeasureDependentStorageLevels](sdk-for-android-explore-com-here-sdk-mapview-maplayermapmeasuredependentstoragelevels "class in com.here.sdk.mapview") mapLayerMapMeasureDependentStorageLevels)</span>

    </div>

    <div class="block">

    Applies a mapping from the map measure to the storage level. This
    mapping is used by the layer to request data for the specified
    storage level corresponding to the map measure from the datasource.
    This can be used for example to fine-tune the resolution of raster
    layers. Note: When the map camera is significantly tilted, the
    storage level is further reduced for data towards the horizon. Note:
    Mappings that request higher storage levels will lead to an
    increased number of requests to the raster tile service. Providing
    the map measure to storage level mapping is optional. If not
    provided, the default mapping will use a storage level that is for
    raster layers one and for others three levels lower than the zoom
    level, corresponding to an offset of -1 and -3.

    </div>

    Parameters:  
    `mapLayerMapMeasureDependentStorageLevels` -

    The map measure to storage level mapping that should be applied for
    the layer.

    Returns:  
    This class instance.

    </div>

  - <div id="withLoadPriority(double)" class="section detail">

    ### withLoadPriority

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayerBuilder](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder "class in com.here.sdk.mapview")</span> <span class="element-name">withLoadPriority</span><span class="parameters">(double loadPriority)</span>

    </div>

    <div class="block">

    Configures the builder to set the layer load priority. Higher load
    priority values lead to layer being scheduled for loading before
    layers with lesser values.

    </div>

    Parameters:  
    `loadPriority` -

    Load priority for layer.

    Returns:  
    This class instance.

    </div>

  - <div id="build()" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[MapLayer](sdk-for-android-explore-com-here-sdk-mapview-maplayer "class in com.here.sdk.mapview")</span> <span class="element-name">build</span>()
    throws
    <span class="exceptions">[MapLayerBuilder.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Constructs, registers and configures a new map layer showing
    specified content type according to the configured parameters. After
    this call this instance is reset to the initial state. It could be
    used to build another map layer, but will not keep any previously
    configured properties.

    </div>

    Returns:  
    A new MapLayer instance.

    Throws:  
    [`MapLayerBuilder.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-maplayerbuilder-instantiationexception "class in com.here.sdk.mapview")
    -

    Indicates an instantiation issue.

    </div>

  </div>

</div>


---
title: "TranslucentMapLayerGroup (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object →
com.here.NativeBasecom.here.sdk.mapview.TranslucentMapLayerGroup →
com.here.NativeBase → com.here.sdk.mapview.TranslucentMapLayerGroup

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">TranslucentMapLayerGroup</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

A translucent layer group that can be the target for
MapLayerPriorityBuilder.inGroup(java.lang.String) . Currently, only
custom line layers can be added to a translucent layer group. Custom
line layers in a translucent layer group are rendered in an offscreen
translucent pass so that overlapping translucent line geometry is not
alpha blended with itself. At creation, the layer group gets added to a
map. The layer group gets removed from the map upon instance destruction
and any layer (categories) still in the group are not rendered anymore,
therefore it is recommended to keep a group alive as long as layers
using the group are alive and in use. Conceptual example to place line
layers into a translucent group: // Create a translucent group with a
unique name and a render priority MapLayerPriority groupPriority = new
MapLayerPriorityBuilder().renderedLast().build();
TranslucentMapLayerGroup group = new
TranslucentMapLayerGroup("TranslucentGroupName", map, groupPriority) //
Create a line layer to be rendered as part of the translucent group
MapLayerPriority lineLayerPriority = new MapLayerPriorityBuilder()
.inGroup("TranslucentGroupName") // places the line layer into the group
.renderedFirst() // to be rendered first when the group is rendered
.withCategory("SomeCategory") // places the line layer category
'SomeCategory' .inGroup("TranslucentGroupName") // into the group
.renderedLast() // to be rendered last when the group is rendered
.build(); MapLayer lineLayer = new MapLayerBuilder()
.withDataSource("DataSourceName", MapContentType.LINE) .forMap(map)
.withName("LineLayerName") .withPriority(lineLayerPriority)
.withStyle(translucentLineStyle) // E.g. "technique": "line" ...
"color": "#FFFFFF80" .build(); // Create a second line layer to be
rendered as part of the translucent group MapLayerPriority
secondLineLayerPriority = new MapLayerPriorityBuilder()
.inGroup("TranslucentGroupName") // places the second line layer into
the group .renderedBeforeLayer("LineLayerName") // to be rendered before
first layer // when the group is rendered .build(); MapLayer
secondLineLayer = new MapLayerBuilder()
.withDataSource("SecondDataSourceName", MapContentType.LINE)
.forMap(map) .withName("SecondLineLayerName")
.withPriority(secondLineLayerPriority)
.withStyle(secondTranslucentLineStyle) // E.g. "technique": "line" ...
"color": "#FFFFFF80" .build(); Note: This is a beta release of this
feature, so there could be a few bugs and unexpected behavior. Related
APIs may change for new releases without a deprecation process.

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

  <a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-errorcode" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup.ErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Error codes for creating the group.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-errordetails" class="type-name-link" title="class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup.ErrorDetails</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Describes the reason for failing to create the group.

  </div>

  </div>

  <div class="col-first even-row-color">

  `static final class `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception" class="type-name-link" title="class in com.here.sdk.mapview"><code>TranslucentMapLayerGroup.InstantiationException</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Thrown when failing to build the group.

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

      TranslucentMapLayerGroup(String name,
       HereMap aMap)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of the group.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      TranslucentMapLayerGroup(String name,
       HereMap aMap,
       MapLayerPriority priority)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates an instance of the group.

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      destroy()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Frees all internally used resources.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `void`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      setPriority(MapLayerPriority priority)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the render priority for the layer group which replaces any
  previously defined priority.

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

  - <div id="sdk-for-android-explore-<init>(java.lang.String,com.here.sdk.mapview.HereMap)"
    class="section detail">

    ### TranslucentMapLayerGroup

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TranslucentMapLayerGroup</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull
    [HereMap](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview") aMap)</span>
    throws
    <span class="exceptions">[TranslucentMapLayerGroup.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates an instance of the group.

    </div>

    Parameters:  
    `name` -

    Name of the group. Must be unique across
    [`MapLayer`](sdk-for-android-explore-com-here-sdk-mapview-maplayer "class in com.here.sdk.mapview")
    and
    [`TranslucentMapLayerGroup`](sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup "class in com.here.sdk.mapview").

    `aMap` -

    The map to attach the group to.

    Throws:  
    [`TranslucentMapLayerGroup.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.lang.String,com.here.sdk.mapview.HereMap,com.here.sdk.mapview.MapLayerPriority)"
    class="section detail">

    ### TranslucentMapLayerGroup

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">TranslucentMapLayerGroup</span><span class="parameters">(@NonNull
    <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> name,
    @NonNull
    [HereMap](sdk-for-android-explore-com-here-sdk-mapview-heremap "class in com.here.sdk.mapview") aMap,
    @NonNull
    [MapLayerPriority](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview") priority)</span>
    throws
    <span class="exceptions">[TranslucentMapLayerGroup.InstantiationException](sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")</span>

    </div>

    <div class="block">

    Creates an instance of the group.

    </div>

    Parameters:  
    `name` -

    Name of the group. Must be unique across
    [`MapLayer`](sdk-for-android-explore-com-here-sdk-mapview-maplayer "class in com.here.sdk.mapview")
    and
    [`TranslucentMapLayerGroup`](sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup "class in com.here.sdk.mapview").

    `aMap` -

    The map to attach the group to.

    `priority` -

    The
    [`MapLayerPriority`](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview")
    which should be applied to position the group. The
    [`MapLayerPriority`](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview")
    must contain only one priority and this priority must have no
    category and no group, i.e.
    [](sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder#inGroup(java.lang.String))

        MapLayerPriorityBuilder.inGroup(java.lang.String)

    and
    [](sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String))

        MapLayerPriorityBuilder.withCategory(java.lang.String)

    should not be used when building the
    [`MapLayerPriority`](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview").
    Example:

        new MapLayerPriorityBuilder().renderedAfterLayer("water").build()

    Throws:  
    [`TranslucentMapLayerGroup.InstantiationException`](sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup-instantiationexception "class in com.here.sdk.mapview")

    In case of invalid input parameters.

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail"
  class="section method-details">

  - <div id="sdk-for-android-explore-setPriority(com.here.sdk.mapview.MapLayerPriority)"
    class="section detail">

    ### setPriority

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">setPriority</span><span class="parameters">(@NonNull
    [MapLayerPriority](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview") priority)</span>

    </div>

    <div class="block">

    Sets the render priority for the layer group which replaces any
    previously defined priority.

    </div>

    Parameters:  
    `priority` -

    The priority to position the group. The
    [`MapLayerPriority`](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview")
    must contain only one priority and this priority must have no
    category and no group, i.e.
    [](sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder#inGroup(java.lang.String))

        MapLayerPriorityBuilder.inGroup(java.lang.String)

    and
    [](sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder#withCategory(java.lang.String))

        MapLayerPriorityBuilder.withCategory(java.lang.String)

    should not be used when building the
    [`MapLayerPriority`](sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority "class in com.here.sdk.mapview").
    Example:

        new MapLayerPriorityBuilder().renderedAfterLayer("water").build()

    </div>

  - <div id="sdk-for-android-explore-destroy()" class="section detail">

    ### destroy

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">destroy</span>()

    </div>

    <div class="block">

    Frees all internally used resources. After calling this method, the
    object is not usable anymore.

    </div>

    </div>

  </div>

</div>


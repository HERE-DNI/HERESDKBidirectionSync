---
title: "MapLayerPriorityBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapLayerPriorityBuilder → com.here.NativeBase com.here.sdk.mapview.MapLayerPriorityBuilder → com.here.sdk.mapview.MapLayerPriorityBuilder

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">MapLayerPriorityBuilder</span> <span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs. Map layers are rendered in an order according to specified priorities. Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer's default, main category is unnamed. The concept of 'category' is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category 'bridges' and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer diffenrently then it should opt for a layer with only the default category (e.g. raster layer). One way to define layers' priorities is by using a layer priority list in the scene configuration. For example, a priority list in a scene configuration could define: background water roads:outline roads labels This means layer "background" is rendered first. Next up is layer "water". Then category "outline" of layer "roads", followed by the main category of layer "roads". Layer "labels" is then rendered last. Now let's consider a newly created layer 'zone' and its categories: zone zone:background zone:lines-outline zone:lines The user wants to alter the rendering order so that it looks like: background water zone:background zone road:outline road zone:lines-outline zone:lines labels This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its renderedBeforeLayer() and renderedAfterLayer() member functions. Note that the order of calls matters and one can use a previously defined layer or category as a reference: MapLayerPriority zoneLayerPriority = new MapLayerPriorityBuilder() .renderedAfterLayer("water") // places "zone" after "water" // in the rendering order .withCategory("background") .renderedAfterLayer("water") // places "zone:background" after "water" // in the rendering order and thus shifts // "zone" to be rendered later .withCategory("lines-outline") .renderedAfterLayer("road") // places "zone:lines-outline" after "road" // in the rendering order .withCategory("lines") .renderedAfterLayer("zone", "lines-outline") // places "zone:lines" after // "zone:lines-outline" in the rendering order .build(); zoneLayer.setPriority(zoneLayerPriority); // applies the priority to the zone layer // and its categories in one single operation. In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer is going to be rendered last. Due to a current limitation for point map layers, the mentioned APIs to control the rendering order are not implemented. All labels will be rendered within the "labels" layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour: 'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels. 'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels. 'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of data: points, lines, polygons.

</div>

</div>

- <div id="sdk-for-android-explore-constructor-summary" class="section constructor-summary">

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

      MapLayerPriorityBuilder ()

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates an instance of the layer priority builder interface.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

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

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">`MapLayerPriority`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      build ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Constructs a MapLayerPriority.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      inGroup ( String group)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the group for which a priority could be defined with the next call to the functions renderedFirst\|Last\|BeforeLayer\|AfterLayer .

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      renderedAfterLayer ( String referenceLayer)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the priority as rendered after the last one from the referenceLayer and its categories.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      renderedAfterLayer ( String referenceLayer, String referenceCategory)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the priority as rendered after the referenceCategory of the referenceLayer.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      renderedBeforeLayer ( String referenceLayer)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the priority as rendered before the first one from the referenceLayer and its categories.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      renderedBeforeLayer ( String referenceLayer, String referenceCategory)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the priority as rendered before the referenceCategory of the referenceLayer.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      renderedFirst ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the priority as rendered before all layers and categories.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      renderedLast ()

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the priority as rendered after all layers and categories.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">`MapLayerPriorityBuilder`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withCategory ( String category)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Sets the layer category for which a priority could be defined with the next call to the functions renderedFirst\|Last\|BeforeLayer\|AfterLayer .

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

- <div id="sdk-for-android-explore-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-explore-init" class="section detail">

    ### MapLayerPriorityBuilder

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapLayerPriorityBuilder</span>()

    </div>

    <div class="block">

    Creates an instance of the layer priority builder interface.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-withCategory-java-lang-String" class="section detail">

    ### withCategory

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">withCategory</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> category)</span>

    </div>

    <div class="block">

    Sets the layer category for which a priority could be defined with the next call to the functions renderedFirst\|Last\|BeforeLayer\|AfterLayer . After a priority is defined by calling one of the aforementioned functions, the current category is cleared and the builder refers again to the layer itself.

    </div>

    Parameters:  
    `category` -

    The name of the layer category.

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-inGroup-java-lang-String" class="section detail">

    ### inGroup

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">inGroup</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> group)</span>

    </div>

    <div class="block">

    Sets the group for which a priority could be defined with the next call to the functions renderedFirst\|Last\|BeforeLayer\|AfterLayer . When a group is set, the next defined priority is relative to the layers and layer categories inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority are only searched inside the group. Only one group or no group can be defined per layer priority and layer category priority, however, different layers can set priorities for the same group. After a priority is defined by calling one of the aforementioned functions, the current group is cleared and the builder refers again to the global layer list in the scene. Note that a group needs to exist when the built MapLayerPriority is used during a MapLayerBuilder.build() or MapLayer.setPriority(com.here.sdk.mapview.MapLayerPriority) , otherwise the priority cannot be applied and the layer will render nothing to the group. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.

    </div>

    Parameters:  
    `group` -

    The name of the group. For instance the name of a <a href="sdk-for-android-explore-com-here-sdk-mapview-translucentmaplayergroup" title="class in com.here.sdk.mapview">`TranslucentMapLayerGroup`</a>.

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-renderedFirst" class="section detail">

    ### renderedFirst

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">renderedFirst</span>()

    </div>

    <div class="block">

    Sets the priority as rendered before all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to withCategory(java.lang.String) . Notice that the order of calls to the functions renderedFirst\|Last\|Before\|After matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like withCategory(\&quot;C\&quot;).renderedAfterLayer(\&quot;L\&quot;).withCategory(\&quot;C\&quot;).renderedBeforeLayer(\&quot;L\&quot;) The previously defined and prioritised categories can be used as reference.

    </div>

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-renderedLast" class="section detail">

    ### renderedLast

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">renderedLast</span>()

    </div>

    <div class="block">

    Sets the priority as rendered after all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to withCategory(java.lang.String) . Notice that the order of calls to the functions renderedFirst\|Last\|Before\|After matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like withCategory(\&quot;C\&quot;).renderedAfterLayer(\&quot;L\&quot;).withCategory(\&quot;C\&quot;).renderedBeforeLayer(\&quot;L\&quot;) The previously defined and prioritised categories can be used as reference.

    </div>

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-renderedBeforeLayer-java-lang-String" class="section detail">

    ### renderedBeforeLayer

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">renderedBeforeLayer</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> referenceLayer)</span>

    </div>

    <div class="block">

    Sets the priority as rendered before the first one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to withCategory(java.lang.String) . Notice that the order of calls to the functions renderedFirst\|Last\|Before\|After matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like withCategory(\&quot;C\&quot;).renderedAfterLayer(\&quot;L\&quot;).withCategory(\&quot;C\&quot;).renderedBeforeLayer(\&quot;L\&quot;) The previously defined and prioritised categories can be used as reference. If the referenceLayer does not exist, then the function will set the priority as rendered before all layers and categories.

    </div>

    Parameters:  
    `referenceLayer` -

    The beforehand defined layer name which renders directly after the current layer.

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-renderedBeforeLayer-java-lang-String-java-lang-String" class="section detail">

    ### renderedBeforeLayer

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">renderedBeforeLayer</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> referenceLayer, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> referenceCategory)</span>

    </div>

    <div class="block">

    Sets the priority as rendered before the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to withCategory(java.lang.String) . Notice that the order of calls to the functions renderedFirst\|Last\|Before\|After matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like withCategory(\&quot;C\&quot;).renderedAfterLayer(\&quot;L\&quot;).withCategory(\&quot;C\&quot;).renderedBeforeLayer(\&quot;L\&quot;) The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered before all layers and categories.

    </div>

    Parameters:  
    `referenceLayer` -

    The beforehand defined layer name which renders directly after the current layer.

    `referenceCategory` -

    The beforehand defined category name which renders directly after the current layer.

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-renderedAfterLayer-java-lang-String" class="section detail">

    ### renderedAfterLayer

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">renderedAfterLayer</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> referenceLayer)</span>

    </div>

    <div class="block">

    Sets the priority as rendered after the last one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to withCategory(java.lang.String) . Notice that the order of calls to the functions renderedFirst\|Last\|Before\|After matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like withCategory(\&quot;C\&quot;).renderedAfterLayer(\&quot;L\&quot;).withCategory(\&quot;C\&quot;).renderedBeforeLayer(\&quot;L\&quot;) The previously defined and prioritised categories can be used as reference. If the referenceLayer does not exist, then the function will set the priority as rendered after all layers and categories.

    </div>

    Parameters:  
    `referenceLayer` -

    The beforehand defined layer name which renders directly before the current layer.

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-renderedAfterLayer-java-lang-String-java-lang-String" class="section detail">

    ### renderedAfterLayer

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerprioritybuilder" title="class in com.here.sdk.mapview">MapLayerPriorityBuilder</a></span> <span class="element-name">renderedAfterLayer</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> referenceLayer, @NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> referenceCategory)</span>

    </div>

    <div class="block">

    Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to withCategory(java.lang.String) . Notice that the order of calls to the functions renderedFirst\|Last\|Before\|After matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like withCategory(\&quot;C\&quot;).renderedAfterLayer(\&quot;L\&quot;).withCategory(\&quot;C\&quot;).renderedBeforeLayer(\&quot;L\&quot;) The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered after all layers and categories.

    </div>

    Parameters:  
    `referenceLayer` -

    The beforehand defined layer name which renders directly before the current layer.

    `referenceCategory` -

    The beforehand defined category name which renders directly before the current layer.

    Returns:  
    This class instance.

    </div>

  - <div id="sdk-for-android-explore-build" class="section detail">

    ### build

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-maplayerpriority" title="class in com.here.sdk.mapview">MapLayerPriority</a></span> <span class="element-name">build</span>()

    </div>

    <div class="block">

    Constructs a MapLayerPriority. The builder is then empty and can be re-used to generate a new MapLayerPriority.

    </div>

    Returns:  
    A new MapLayerPriority instance.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


---
title: "Map Layer Priority Builder"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapLayerPriorityBuilder///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/MapLayerPriorityBuilder</div>
<div class="cover">
<h1 class="cover">Map<wbr/>Layer<wbr/>Priority<wbr/>Builder</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder : /sdk-for-flutter-explore-a-p-i-reference-com-here-native-base</div><p class="paragraph">MapLayerPriorityBuilder is an interface used to define the rendering priority of a layer and its categories, relative to other layers or layer-category pairs.</p><p class="paragraph">Map layers are rendered in an order according to specified priorities. Rendering order of elements in a single map layer can be controlled with categories. Layer names are unique, and category names have to be unique within a layer. The layer's default, main category is unnamed.</p><p class="paragraph">The concept of 'category' is tightly linked to styling. The idea behind category is that one should be able to style separately elements in a map layer. Take, for instance, roads. If one wants to style separately the bridges it will create a category 'bridges' and style it accordingly in the style file. If the user does not intend to or cannot style elements of the layer diffenrently then it should opt for a layer with only the default category (e.g. raster layer).</p><p class="paragraph">One way to define layers' priorities is by using a layer priority list in the scene configuration.</p><p class="paragraph">For example, a priority list in a scene configuration could define:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">roads:outline</p></li><li><p class="paragraph">roads</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">This means layer "background" is rendered first. Next up is layer "water". Then category "outline" of layer "roads", followed by the main category of layer "roads". Layer "labels" is then rendered last.</p><p>
Now let's consider a newly created layer 'zone' and its categories:<ul><li><p class="paragraph">zone</p></li><li><p class="paragraph">zone:background</p></li><li><p class="paragraph">zone:lines-outline</p></li><li><p class="paragraph">zone:lines</p></li></ul><p class="paragraph">The user wants to alter the rendering order so that it looks like:</p><ul><li><p class="paragraph">background</p></li><li><p class="paragraph">water</p></li><li><p class="paragraph">zone:background</p></li><li><p class="paragraph">zone</p></li><li><p class="paragraph">road:outline</p></li><li><p class="paragraph">road</p></li><li><p class="paragraph">zone:lines-outline</p></li><li><p class="paragraph">zone:lines</p></li><li><p class="paragraph">labels</p></li></ul><p class="paragraph">This could be achieved with the help of the MapLayerPriorityBuilder and a sequence of calls to its <code class="lang-kotlin">renderedBeforeLayer()</code> and <code class="lang-kotlin">renderedAfterLayer()</code> member functions.</p><p class="paragraph">Note that the order of calls matters and one can use a previously defined layer or category as a reference:</p><p class="paragraph">In case an empty MapLayerPriority without any ordering commands is built, it is assumed that the target layer is going to be rendered last.</p><p class="paragraph">Due to a current limitation for point map layers, the mentioned APIs to control the rendering order are not implemented. All labels will be rendered within the "labels" layer, defined in the scene configuration file. By default, all labels rendered by a point map layer are rendered last and no overlapping is allowed. The following categories can be used to have a different behaviour:</p><ul><li><p class="paragraph">'custom-labels' A label should be rendered first, is allowed to overlap with other labels of the same category and block map labels.</p></li><li><p class="paragraph">'custom-labels-no-self-overlap' A label should be rendered after 'custom-labels', is not allowed to overlap with other labels of the same categoty and block map labels.</p></li><li><p class="paragraph">'custom-labels-overlap-all' A label should be rendered last, is allowed to overlap all predefined categories, also map labels. These categories are configured accordingly in the basic map scene configurations. Category assignment to features can be done in the style based on data attributes. The category assignment can be done for all types of data: points, lines, polygons.</p></li></ul></p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MapLayerPriorityBuilder" data-filterable-set=":modules:dokkaHtml/release" data-name="-1694501189%2FConstructors%2F1617540583" id="-1694501189%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-map-layer-priority-builder</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates an instance of the layer priority builder interface.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="829797604%2FClasslikes%2F1617540583" id="829797604%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="build" data-filterable-set=":modules:dokkaHtml/release" data-name="1959036143%2FFunctions%2F1617540583" id="1959036143%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-build</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-build(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority</div><div class="brief"><p class="paragraph">Constructs a MapLayerPriority. The builder is then empty and can be re-used to generate a new MapLayerPriority.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="inGroup" data-filterable-set=":modules:dokkaHtml/release" data-name="141529441%2FFunctions%2F1617540583" id="141529441%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-in-group</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-in-group(group: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the group for which a priority could be defined with the next call to the functions {@code renderedFirst|Last|BeforeLayer|AfterLayer}. When a group is set, the next defined priority is relative to the layers and layer categories inside this group. The references (i.e. 'referenceLayer' and 'referenceCategory') of the priority are only searched inside the group. Only one group or no group can be defined per layer priority and layer category priority, however, different layers can set priorities for the same group. After a priority is defined by calling one of the aforementioned functions, the current group is cleared and the builder refers again to the global layer list in the scene. Note that a group needs to exist when the built /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority is used during a /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-builder-build or /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-set-priority, otherwise the priority cannot be applied and the layer will render nothing to the group. Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="renderedAfterLayer" data-filterable-set=":modules:dokkaHtml/release" data-name="1800058663%2FFunctions%2F1617540583" id="1800058663%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-after-layer</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-after-layer(referenceLayer: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the priority as rendered after the last one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-after-layer(referenceLayer: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, referenceCategory: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="renderedBeforeLayer" data-filterable-set=":modules:dokkaHtml/release" data-name="-528700639%2FFunctions%2F1617540583" id="-528700639%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-before-layer</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-before-layer(referenceLayer: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the priority as rendered before the first one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-before-layer(referenceLayer: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, referenceCategory: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the priority as rendered before the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="renderedFirst" data-filterable-set=":modules:dokkaHtml/release" data-name="-302913278%2FFunctions%2F1617540583" id="-302913278%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-first</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-first(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the priority as rendered before all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="renderedLast" data-filterable-set=":modules:dokkaHtml/release" data-name="1863041362%2FFunctions%2F1617540583" id="1863041362%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-last</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-last(): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the priority as rendered after all layers and categories. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="withCategory" data-filterable-set=":modules:dokkaHtml/release" data-name="536824107%2FFunctions%2F1617540583" id="536824107%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category(category: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><div class="brief"><p class="paragraph">Sets the layer category for which a priority could be defined with the next call to the functions {@code renderedFirst|Last|BeforeLayer|AfterLayer}. After a priority is defined by calling one of the aforementioned functions, the current category is cleared and the builder refers again to the layer itself.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="footer">
<a class="footer--button footer--button_go-to-top" href="#content" id="go-to-top-link"></a>
© 2026 Copyright

Generated by 
<a class="footer--link footer--link_external" href="https://github.com/Kotlin/dokka">
dokka
</a>

</div>
</div>

</div>

</div>
`
}</HTMLBlock>

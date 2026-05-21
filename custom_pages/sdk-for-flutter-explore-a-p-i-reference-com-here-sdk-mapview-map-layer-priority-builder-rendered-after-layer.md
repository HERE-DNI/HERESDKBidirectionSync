---
title: "rendered After Layer"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-after-layer"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- rendered-after-layer.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="member" id="content" pageids="API Reference::com.here.sdk.mapview/MapLayerPriorityBuilder/renderedAfterLayer/#kotlin.String/PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder/renderedAfterLayer</div>
<div class="cover">
<h1 class="cover">rendered<wbr/>After<wbr/>Layer</h1>
</div>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-after-layer(referenceLayer: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><p class="paragraph">Sets the priority as rendered after the last one from the referenceLayer and its categories. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p><p class="paragraph">{@code withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")}</p><p class="paragraph">The previously defined and prioritised categories can be used as reference. If the referenceLayer does not exist, then the function will set the priority as rendered after all layers and categories.</p><h4 class="">Return</h4><p class="paragraph">This class instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>reference<wbr/>Layer</u></div></div><div><div class="title"><p class="paragraph">The beforehand defined layer name which renders directly before the current layer.</p></div></div></div></div></div><hr/><div class="symbol monospace">external fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-rendered-after-layer(referenceLayer: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, referenceCategory: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder</div><p class="paragraph">Sets the priority as rendered after the referenceCategory of the referenceLayer. Applies to the layer itself or the category pointed to by the preceding call to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-layer-priority-builder-with-category. Notice that the order of calls to the functions {@code renderedFirst|Last|Before|After} matters, and that after such a call the builder clears the current category and refers again to the layer itself. Further, only one priority for each layer and layer category should be set with these functions since previous priorities would be ingored. For example the priority to render layer category 'C' after layer 'L' would be overridden by the priority to render layer category 'C' before layer 'L' when building something like</p><p class="paragraph">{@code withCategory("C").renderedAfterLayer("L").withCategory("C").renderedBeforeLayer("L")}</p><p class="paragraph">The previously defined and prioritised categories can be used as reference. If the referenceLayer and/or the referenceCategory do not exist, then the function will set the priority as rendered after all layers and categories.</p><h4 class="">Return</h4><p class="paragraph">This class instance.</p><h4 class="">Parameters</h4><div class="table"><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>reference<wbr/>Layer</u></div></div><div><div class="title"><p class="paragraph">The beforehand defined layer name which renders directly before the current layer.</p></div></div></div></div><div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release"><div class="main-subrow keyValue"><div class=""><div><u>reference<wbr/>Category</u></div></div><div><div class="title"><p class="paragraph">The beforehand defined category name which renders directly before the current layer.</p></div></div></div></div></div></div></div>
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

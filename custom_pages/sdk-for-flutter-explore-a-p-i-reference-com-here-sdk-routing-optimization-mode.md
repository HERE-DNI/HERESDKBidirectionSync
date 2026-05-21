---
title: "Optimization Mode"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.routing/OptimizationMode///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing/OptimizationMode</div>
<div class="cover">
<h1 class="cover">Optimization<wbr/>Mode</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode&gt; </div><p class="paragraph">Identifiers for different optimizations that can be used during the route calculation while trying to keep the quality of the route being calculated high. The route is considered to be of low quality if it gives the traveler an unpleasant experience, such as having difficult turns or having a lot of turns in general. For example, if there are two possible routes from A to B, one with a length of 1000m and 10 turns, and another with a length of 1050m and only one turn, the second one will be returned as the shortest, although it is 50m longer. Yet, it contains only one turn and it is therefore considered to provide a better traveler experience.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
<div class="tabs-section-body">
<div data-togglable="ENTRY">
<h2 class="">Entries</h2>
<div class="table"><a anchor-label="FASTEST" data-filterable-set=":modules:dokkaHtml/release" data-name="995700206%2FClasslikes%2F1617540583" id="995700206%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-f-a-s-t-e-s-t</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-f-a-s-t-e-s-t</div></div><div class="brief"><p class="paragraph">The routing algorithm will attempt to find the fastest route possible, i.e. to optimize travel time while at the same time keeping the quality of the route high. For example, the algorithm may favor a route that remains on a highway, even if a shorter route can be achieved by taking a shortcut through side roads.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="SHORTEST" data-filterable-set=":modules:dokkaHtml/release" data-name="1814573902%2FClasslikes%2F1617540583" id="1814573902%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-s-h-o-r-t-e-s-t</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-s-h-o-r-t-e-s-t</div></div><div class="brief"><p class="paragraph">The routing algorithm will attempt to find the shortest route possible, i.e. to optimize the length of the route while at the same time keeping the quality of the route high. For example, the algorithm may favor taking a shortcut that ignores speed information, even if a faster route can be achieved by staying on the highway.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="entries" data-filterable-set=":modules:dokkaHtml/release" data-name="-1958623522%2FProperties%2F1617540583" id="-1958623522%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-entries</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-entries: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode&gt;</div><div class="brief"><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="value" data-filterable-set=":modules:dokkaHtml/release" data-name="548340061%2FProperties%2F1617540583" id="548340061%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-value</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="valueOf" data-filterable-set=":modules:dokkaHtml/release" data-name="-328159362%2FFunctions%2F1617540583" id="-328159362%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-value-of</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-value-of(value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode</div><div class="brief"><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="values" data-filterable-set=":modules:dokkaHtml/release" data-name="1384927498%2FFunctions%2F1617540583" id="1384927498%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-values</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode-values(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-routing-optimization-mode&gt;</div><div class="brief"><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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

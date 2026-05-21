---
title: "Options"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core/PolylineSimplifier.Options///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier/Options</div>
<div class="cover">
<h1 class="cover">Options</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options</div><p class="paragraph">Controls the strategy of /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-simplify when reducing a size of polyline.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="Options" data-filterable-set=":modules:dokkaHtml/release" data-name="-1101522905%2FConstructors%2F1617540583" id="-1101522905%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-options</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates default options with /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-max-points equal to 0 and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-simplification-tolerance-in-meters equal to /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-companion-s-i-m-p-l-i-f-i-c-a-t-i-o-n-i-n-m-e-t-e-r-s-14-z-o-o-m-l-e-v-e-l.</p></div><div class="symbol monospace">constructor(maxPoints: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>, simplificationToleranceInMeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a>)</div><div class="brief"><p class="paragraph">Creates options with explicitly specified /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-max-points and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-simplification-tolerance-in-meters.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-153401774%2FClasslikes%2F1617540583" id="-153401774%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="maxPoints" data-filterable-set=":modules:dokkaHtml/release" data-name="114291588%2FProperties%2F1617540583" id="114291588%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-max-points</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-max-points: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a></div><div class="brief"><p class="paragraph">Sets the upper limit on the resulting collection for the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-simplify. Lower value results in the lower accuracy of the resulting polyline. If <code class="lang-kotlin">maxPoints</code> is less than <code class="lang-kotlin">2</code> then resulting polyline will not have an upper limit on the size and only /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-simplification-tolerance-in-meters will be considered. When <code class="lang-kotlin">maxPoints</code> is greater than size of the passed polyline then simplification algorithm will take into account only /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-simplification-tolerance-in-meters.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="simplificationToleranceInMeters" data-filterable-set=":modules:dokkaHtml/release" data-name="-1028895654%2FProperties%2F1617540583" id="-1028895654%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-simplification-tolerance-in-meters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-options-simplification-tolerance-in-meters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-long/index.html">Long</a></div><div class="brief"><p class="paragraph">Sets the accuracy limit for the /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-polyline-simplifier-simplify:</p></div></div></div>
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

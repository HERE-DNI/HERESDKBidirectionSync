---
title: "Car Specifications"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.transport/CarSpecifications///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport/CarSpecifications</div>
<div class="cover">
<h1 class="cover">Car<wbr/>Specifications</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications</div><div class="deprecation-content"><h3 class="">Deprecated</h3><p class="paragraph">Will be removed in v4.28.0. Use <code>TransportSpecification</code> instead.</p></div><p class="paragraph">Car specifications contain vehicle related attributes. Examples: Dimensions, weight, axle count. Only the fields that are set are considered for restriction handling.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="CarSpecifications" data-filterable-set=":modules:dokkaHtml/release" data-name="-1093382769%2FConstructors%2F1617540583" id="-1093382769%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-car-specifications</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor()</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="axleCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-196204140%2FProperties%2F1617540583" id="-196204140%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-axle-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-axle-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Defines total number of axles in the vehicle. The provided value must be greater than or equal to 2. By default, it is not set. Route calculation: When not set, possible axle count restrictions will not be taken into consideration. When specifying /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-axle-count, then /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-axle-count is required and must be greater than /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-axle-count.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="grossWeightInKilograms" data-filterable-set=":modules:dokkaHtml/release" data-name="1566990765%2FProperties%2F1617540583" id="1566990765%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-gross-weight-in-kilograms</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-gross-weight-in-kilograms: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Car weight including trailers and shipped goods in kilograms. The provided value must be greater than or equal to 0. By default, it is not set. <strong>Note:</strong> This parameter is limited to a maximum weight of 4250 kg without trailer and 7550 kg with trailer.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="heightInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="-1932664748%2FProperties%2F1617540583" id="-1932664748%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-height-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-height-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Car height in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="lengthInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="1725252307%2FProperties%2F1617540583" id="1725252307%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-length-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-length-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Car length in centimeters. The provided value must be in the range \[0, 30000\]. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="trailerAxleCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-1308385925%2FProperties%2F1617540583" id="-1308385925%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-axle-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-axle-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Defines total number of axles across all the trailers attached to the vehicle. This number is included in /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-axle-count, hence /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-axle-count must be less than /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-axle-count and greater than or equal to 1. /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-axle-count and /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-count are required to specify /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-axle-count. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="trailerCount" data-filterable-set=":modules:dokkaHtml/release" data-name="-405265429%2FProperties%2F1617540583" id="-405265429%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-count</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-count: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Defines number of trailers attached to the vehicle. The provided value must be in the range \[0, 1\]. By default, it is not set. When specifying /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-axle-count, then /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-trailer-count is required and must be greater than 0.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="widthInCentimeters" data-filterable-set=":modules:dokkaHtml/release" data-name="1775357447%2FProperties%2F1617540583" id="1775357447%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-width-in-centimeters</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-width-in-centimeters: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Car width in centimeters. The provided value must be in the range \[0, 5000\]. By default, it is not set.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-1156759974%2FFunctions%2F1617540583" id="-1156759974%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-1675068084%2FFunctions%2F1617540583" id="-1675068084%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-transport-car-specifications-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
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

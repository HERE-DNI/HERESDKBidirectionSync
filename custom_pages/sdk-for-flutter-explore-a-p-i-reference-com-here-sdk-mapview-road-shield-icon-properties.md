---
title: "Road Shield Icon Properties"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/RoadShieldIconProperties///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview/RoadShieldIconProperties</div>
<div class="cover">
<h1 class="cover">Road<wbr/>Shield<wbr/>Icon<wbr/>Properties</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties</div><p class="paragraph">Contains the information required to create a road shield image.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="RoadShieldIconProperties" data-filterable-set=":modules:dokkaHtml/release" data-name="-1335309188%2FConstructors%2F1617540583" id="-1335309188%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-road-shield-icon-properties</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(routeType: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-route-type, countryCode: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, stateCode: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, routeNumberName: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>, shieldText: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>)</div><div class="brief"><p class="paragraph">Creates a new instance.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="countryCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-1904826399%2FProperties%2F1617540583" id="-1904826399%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-country-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-country-code: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">The country code in ISO-3166-1 alpha-3 format, which will determine the type of road shield.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routeNumberName" data-filterable-set=":modules:dokkaHtml/release" data-name="-2017582169%2FProperties%2F1617540583" id="-2017582169%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-route-number-name</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-route-number-name: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">A string that is used to additionally determine the road shield's visual representation. In a routing context, the text can be taken from a <code class="lang-kotlin">LocalizedRoadNumber</code>, which is available for each <code class="lang-kotlin">Span</code> of a <code class="lang-kotlin">Route</code> object. Typically, the string contains the number of a road, such as "E100". Internally, the text is parsed with a RegEx pattern and the results will be used along with other properties such as <code class="lang-kotlin">routeType</code>, <code class="lang-kotlin">countryCode</code> and <code class="lang-kotlin">stateCode</code> to identify the visual representation of a road shield icon.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="routeType" data-filterable-set=":modules:dokkaHtml/release" data-name="1343159073%2FProperties%2F1617540583" id="1343159073%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-route-type</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-route-type: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-route-type</div><div class="brief"><p class="paragraph">The type of route indicating the significance of the road in a range from 0 to 6. A value of 1 stands for the most major route and 6 the most minor, with 0 being of unknown type.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="shieldText" data-filterable-set=":modules:dokkaHtml/release" data-name="2008273408%2FProperties%2F1617540583" id="2008273408%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-shield-text</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-shield-text: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">The text of the road-shield. This is the text which is displayed on the road-shield in reality. It will be in the output road-shield icon.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="stateCode" data-filterable-set=":modules:dokkaHtml/release" data-name="-2007290234%2FProperties%2F1617540583" id="-2007290234%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-state-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-road-shield-icon-properties-state-code: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div><div class="brief"><p class="paragraph">The state code for the road. It's a 2-letter code in ISO 3166-2 format. For example the ones listed for US on this page https://en.wikipedia.org/wiki/ISO_3166-2:US. The code "AL" is for Alabama. Another example is the code for autonomous communities listed on https://en.wikipedia.org/wiki/ISO_3166-2:ES. Can be empty if not required for the particular country.</p></div></div></div>
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

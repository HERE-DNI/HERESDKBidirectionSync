---
title: "EVSEState"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.ev/EVSEState///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev/EVSEState</div>
<div class="cover">
<h1 class="cover">EVSEState</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">enum /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state : <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-enum/index.html">Enum</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state&gt; </div><p class="paragraph">Indicates the current short-term status of the EVSE at the time given in the modified property. There are no separate statuses available for individual connectors. A single EVSE can only be used by a single car, so same statuses apply to other connectors as well. So, if one connector is in use, the whole EVSE has status charging, and other connectors cannot be used at the same time, hence they should be considered in-use as well. If an EVSE can allow multiple connectors to be used at the same time, it is basically multiple EVSEs merged into a single physical box or device.</p><p class="paragraph"><strong>Note:</strong> This is a beta release of this feature, so there could be a few bugs and unexpected behaviors. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button><button class="section-tab" data-togglable="ENTRY">Entries</button></div>
<div class="tabs-section-body">
<div data-togglable="ENTRY">
<h2 class="">Entries</h2>
<div class="table"><a anchor-label="UNKNOWN" data-filterable-set=":modules:dokkaHtml/release" data-name="827314565%2FClasslikes%2F1617540583" id="827314565%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-u-n-k-n-o-w-n</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-u-n-k-n-o-w-n</div></div><div class="brief"><p class="paragraph">No status information available or the EVSE/connector is offline.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="AVAILABLE" data-filterable-set=":modules:dokkaHtml/release" data-name="-1560731132%2FClasslikes%2F1617540583" id="-1560731132%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-a-v-a-i-l-a-b-l-e</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-a-v-a-i-l-a-b-l-e</div></div><div class="brief"><p class="paragraph">The EVSE/connector is able to start a new charging session.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="BLOCKED" data-filterable-set=":modules:dokkaHtml/release" data-name="-533469273%2FClasslikes%2F1617540583" id="-533469273%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-b-l-o-c-k-e-d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-b-l-o-c-k-e-d</div></div><div class="brief"><p class="paragraph">The EVSE/connector is not accessible because of a physical barrier, i.e. a car.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="CHARGING" data-filterable-set=":modules:dokkaHtml/release" data-name="831478750%2FClasslikes%2F1617540583" id="831478750%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-c-h-a-r-g-i-n-g</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-c-h-a-r-g-i-n-g</div></div><div class="brief"><p class="paragraph">The EVSE/connector is in use.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="INOPERATIVE" data-filterable-set=":modules:dokkaHtml/release" data-name="-587993491%2FClasslikes%2F1617540583" id="-587993491%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-i-n-o-p-e-r-a-t-i-v-e</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-i-n-o-p-e-r-a-t-i-v-e</div></div><div class="brief"><p class="paragraph">The EVSE/connector is temporarily not available for use, but not broken or defect.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="OUT_OF_ORDER" data-filterable-set=":modules:dokkaHtml/release" data-name="-686506204%2FClasslikes%2F1617540583" id="-686506204%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-o-u-t-o-f-o-r-d-e-r</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-o-u-t-o-f-o-r-d-e-r</div></div><div class="brief"><p class="paragraph">The EVSE/connector is currently out of order.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="RESERVED" data-filterable-set=":modules:dokkaHtml/release" data-name="1573246549%2FClasslikes%2F1617540583" id="1573246549%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-r-e-s-e-r-v-e-d</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-r-e-s-e-r-v-e-d</div></div><div class="brief"><p class="paragraph">The EVSE/connector is reserved for a particular EV driver and is unavailable for other drivers.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="OPERATIONAL" data-filterable-set=":modules:dokkaHtml/release" data-name="-2039736435%2FClasslikes%2F1617540583" id="-2039736435%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="ENTRY">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-o-p-e-r-a-t-i-o-n-a-l</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block">/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-o-p-e-r-a-t-i-o-n-a-l</div></div><div class="brief"><p class="paragraph">The EVSE/connector was operational when checked the last time, but the actual latest status is not available at the moment.</p></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="PROPERTY">
<h2 class="">Properties</h2>
<div class="table"><a anchor-label="entries" data-filterable-set=":modules:dokkaHtml/release" data-name="1232757127%2FProperties%2F1617540583" id="1232757127%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-entries</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-entries: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.enums/-enum-entries/index.html">EnumEntries</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state&gt;</div><div class="brief"><p class="paragraph">Returns a representation of an immutable list of all enum entries, in the order they're declared.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="value" data-filterable-set=":modules:dokkaHtml/release" data-name="1248866886%2FProperties%2F1617540583" id="1248866886%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-value</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>val /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="valueOf" data-filterable-set=":modules:dokkaHtml/release" data-name="-1880330379%2FFunctions%2F1617540583" id="-1880330379%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-value-of</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-value-of(value: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a>): /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state</div><div class="brief"><p class="paragraph">Returns the enum constant of this type with the specified name. The string must match exactly an identifier used to declare an enum constant in this type. (Extraneous whitespace characters are not permitted.)</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="values" data-filterable-set=":modules:dokkaHtml/release" data-name="1626422593%2FFunctions%2F1617540583" id="1626422593%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-values</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state-values(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-array/index.html">Array</a>&lt;/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-ev-e-v-s-e-state&gt;</div><div class="brief"><p class="paragraph">Returns an array containing the constants of this enum type, in the order they're declared.</p></div></div></div>
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

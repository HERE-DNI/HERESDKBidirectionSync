---
title: "Color"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.core/Color///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core/Color</div>
<div class="cover">
<h1 class="cover">Color</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color(fred: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>, fgreen: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>, fblue: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>, falpha: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>)</div><p class="paragraph">Represents a color value.</p><p class="paragraph">The class is compatible with the native package <code class="lang-kotlin">android.graphics</code> and replaces native class <a href="https://developer.android.com/reference/kotlin/android/graphics/Color.html">android.graphics.Color</a>.</p><h3 class="">Usage example:</h3><div class="sample-container"><pre><code class="block lang-kotlin" theme="idea">import com.here.sdk.core.Color<br/>import android.graphics.Color.BLUE<br/>import android.graphics.Color.green<br/><br/>// Convert native colors to HERE color.<br/>val blue = Color.valueOf(android.graphics.Color.BLUE)<br/>val anotherColor = Color.valueOf(0.25f, 0.5f, 0.75f, 0.9f) // ARGB<br/>// Retrieve the blue color component.<br/>val blueColorValue = anotherColor.blue() // = 0.9f<br/>// Convert back to a native color component with the range [0,255].<br/>val greenColorValue = android.graphics.Color.green(anotherColor.toArgb()) // = 230</code></pre><div class="copy-popup-wrapper popup-to-left">Content copied to clipboard</div></div></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="Color" data-filterable-set=":modules:dokkaHtml/release" data-name="-993526962%2FConstructors%2F1617540583" id="-993526962%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-color</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">constructor(fred: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>, fgreen: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>, fblue: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>, falpha: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a>)</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="TYPE">
<h2 class="">Types</h2>
<div class="table"><a anchor-label="Companion" data-filterable-set=":modules:dokkaHtml/release" data-name="-1793263205%2FClasslikes%2F1617540583" id="-1793263205%2FClasslikes%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-companion</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">object /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-companion</div></div></div>
</div>
</div>
</div>
</div>
</div>
</div>
<div data-togglable="FUNCTION">
<h2 class="">Functions</h2>
<div class="table"><a anchor-label="alpha" data-filterable-set=":modules:dokkaHtml/release" data-name="346816566%2FFunctions%2F1617540583" id="346816566%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-alpha</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-alpha(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="blue" data-filterable-set=":modules:dokkaHtml/release" data-name="121988524%2FFunctions%2F1617540583" id="121988524%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-blue</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-blue(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="equals" data-filterable-set=":modules:dokkaHtml/release" data-name="-720066053%2FFunctions%2F1617540583" id="-720066053%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-equals</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open operator override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-equals(other: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-any/index.html">Any</a>?): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-boolean/index.html">Boolean</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="green" data-filterable-set=":modules:dokkaHtml/release" data-name="598873649%2FFunctions%2F1617540583" id="598873649%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-green</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-green(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="hashCode" data-filterable-set=":modules:dokkaHtml/release" data-name="2143832203%2FFunctions%2F1617540583" id="2143832203%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-hash-code</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-hash-code(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="red" data-filterable-set=":modules:dokkaHtml/release" data-name="-283213277%2FFunctions%2F1617540583" id="-283213277%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-red</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-red(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-float/index.html">Float</a></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="toArgb" data-filterable-set=":modules:dokkaHtml/release" data-name="2020819583%2FFunctions%2F1617540583" id="2020819583%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-to-argb</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://developer.android.com/reference/kotlin/androidx/annotation/ColorInt.html">ColorInt</a></div></div>fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-to-argb(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a></div><div class="brief"><p class="paragraph">Converts this color to an ARGB color int.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="toString" data-filterable-set=":modules:dokkaHtml/release" data-name="1965666138%2FFunctions%2F1617540583" id="1965666138%2FFunctions%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-to-string</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">open override fun /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-core-color-to-string(): <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-string/index.html">String</a></div></div></div>
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

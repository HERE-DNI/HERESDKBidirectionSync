---
title: "Untitled"
slug: "sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- index.html -->

<div class="root">



<div id="main">
<div class="main-content" data-page-type="classlike" id="content" pageids="API Reference::com.here.sdk.mapview/MapContext.MemoryManagementOptions///PointingToDeclaration//1617540583">
<div class="breadcrumbs">/sdk-for-flutter-explore//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview//sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context/MemoryManagementOptions</div>
<div class="cover">
<h1 class="cover">Memory<wbr/>Management<wbr/>Options</h1>
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace">class /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options</div><p class="paragraph">Memory management options.</p><p class="paragraph">Note: This is a beta release of this feature, so there could be a few bugs and unexpected behavior. Related APIs may change for new releases without a deprecation process.</p></div></div>
</div>
<div class="tabbedcontent">
<div class="tabs-section" tabs-section="tabs-section"><button class="section-tab" data-active="" data-togglable="CONSTRUCTOR,TYPE,PROPERTY,FUNCTION">Members</button></div>
<div class="tabs-section-body">
<div data-togglable="CONSTRUCTOR">
<h2 class="">Constructors</h2>
<div class="table"><a anchor-label="MemoryManagementOptions" data-filterable-set=":modules:dokkaHtml/release" data-name="1195456320%2FConstructors%2F1617540583" id="1195456320%2FConstructors%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release" data-togglable="CONSTRUCTOR">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-memory-management-options</div>

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
<div class="table"><a anchor-label="memoryManagementStrategy" data-filterable-set=":modules:dokkaHtml/release" data-name="-1965131895%2FProperties%2F1617540583" id="-1965131895%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-memory-management-strategy</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-memory-management-strategy: /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-strategy</div><div class="brief"><p class="paragraph">The default setting MemoryManagementStrategy.DYNAMIC is suitable for common cases. The map data cache can adjust dynamically to fit visible data. When the visible data needs extra memory, it would increase. When it's not needed, it will reduce to a limit which is calculated internally or by using /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-tile-cache-memory-limit-in-ki-b option. The MemoryManagementStrategy.FIXED would be only useful when there is very strict memory consumption requirement for the application. It potentially can have flickering visual artifacts when the map data to be visualized is very large and exceeds the cache limit.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="tileCacheMemoryLimitInKiB" data-filterable-set=":modules:dokkaHtml/release" data-name="503979233%2FProperties%2F1617540583" id="503979233%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-tile-cache-memory-limit-in-ki-b</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-tile-cache-memory-limit-in-ki-b: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Tile cache memory limit in kibibytes. Non positive or <code class="lang-kotlin">null</code> values are ignored. Default value is <code class="lang-kotlin">null</code>. Low tile cache limit will lead to eviction of tiles only if MemoryManagementStrategy is set to FIXED.</p></div></div></div>
</div>
</div>
</div>
</div>
<a anchor-label="videoMemoryLimitInKiB" data-filterable-set=":modules:dokkaHtml/release" data-name="-1028477894%2FProperties%2F1617540583" id="-1028477894%2FProperties%2F1617540583"></a>
<div class="table-row" data-filterable-current=":modules:dokkaHtml/release" data-filterable-set=":modules:dokkaHtml/release">
<div class="main-subrow keyValue">
<div class="">
<div>/sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-video-memory-limit-in-ki-b</div>

<div class="copy-popup-wrapper">Link copied to clipboard</div>
</div>
<div>
<div class="title">
<div class="platform-hinted" data-platform-hinted="data-platform-hinted"><div class="content sourceset-dependent-content" data-active="" data-togglable=":modules:dokkaHtml/release"><div class="symbol monospace"><div class="block"><div class="block">@<a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin.jvm/-jvm-field/index.html">JvmField</a></div></div>var /sdk-for-flutter-explore-a-p-i-reference-com-here-sdk-mapview-map-context-memory-management-options-video-memory-limit-in-ki-b: <a href="https://kotlinlang.org/api/core/kotlin-stdlib/kotlin/-int/index.html">Int</a>?</div><div class="brief"><p class="paragraph">Target video memory limit in kibibytes. Non positive or <code class="lang-kotlin">null</code> values are ignored. Default value is <code class="lang-kotlin">null</code>.</p></div></div></div>
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

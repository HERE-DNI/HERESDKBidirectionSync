---
title: "getInstalledRegions abstract method"
slug: "sdk-for-flutter-navigate-maploader-mapdownloader-getinstalledregions"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- getInstalledRegions.html -->
<div class="doc-with-sidebar"><div class="doc-content">
<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">getInstalledRegions abstract method</li>
</ol>
<div class="self-name">getInstalledRegions</div>
<form class="search navbar-right" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-box" placeholder="Loading search..." type="text"/>
</form>
<div class="toggle" id="theme-button" title="Toggle brightness">
<label for="theme">
<input id="theme" type="checkbox" value="light-theme"/>

        dark_mode
      

        light_mode
      
</label>
</div>
</header>
<main>
<div class="main-content" data-above-sidebar="maploader/MapDownloader-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>getInstalledRegions abstract method</h1></div>
<section class="multi-line-signature">
List&lt;<wbr/>/sdk-for-flutter-navigate-maploader-installedregion-class&gt;
getInstalledRegions(<wbr/>)

      

    </section>
<section class="desc markdown">
<p>Method to get a list of map regions that are currently installed on the device.</p>
<p>Throws if it's not possible to return list of installed regions.
Returned list contains:</p>
<ul>
<li>successfully downloaded regions, indicated by /sdk-for-flutter-navigate-maploader-installedregionstatus in /sdk-for-flutter-navigate-maploader-installedregion-status;</li>
<li>regions, that are in the download process, indicated by /sdk-for-flutter-navigate-maploader-installedregionstatus in /sdk-for-flutter-navigate-maploader-installedregion-status;</li>
<li>regions, which were failed to be downloaded, indicated by /sdk-for-flutter-navigate-maploader-installedregionstatus in /sdk-for-flutter-navigate-maploader-installedregion-status.
Note: precise Japan content is stored in separate catalog on the HERE platform, and when corresponding region is downloaded, then the status of siblings and parent regions is
set to the /sdk-for-flutter-navigate-maploader-installedregionstatus in /sdk-for-flutter-navigate-maploader-installedregion-status. Precise Japan content is available as an additional offering, please contact sales team for more information.</li>
</ul>
<p>Returns <code>List&lt;InstalledRegion&gt;</code>. List of IDs of regions that are installed on the device</p>
<p>Throws /sdk-for-flutter-navigate-maploader-maploaderexceptionexception-class. Specifies reason, why list of installed regions is not returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;InstalledRegion&gt; getInstalledRegions();</code></pre>
</section>
</div>
<div class="sidebar sidebar-offcanvas-left" id="dartdoc-sidebar-left">
<header class="hidden-l" id="header-search-sidebar">
<form class="search-sidebar" role="search">
<input autocomplete="off" class="form-control typeahead" disabled="" id="search-sidebar" placeholder="Loading search..." type="text"/>
</form>
</header>
<ol class="breadcrumbs gt-separated dark hidden-l" id="sidebar-nav">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-maploader-maploader-library</li>
<li>/sdk-for-flutter-navigate-maploader-mapdownloader-class</li>
<li class="self-crumb">getInstalledRegions abstract method</li>
</ol>
<h5>MapDownloader class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>
</div></div>
</div>
`
}</HTMLBlock>

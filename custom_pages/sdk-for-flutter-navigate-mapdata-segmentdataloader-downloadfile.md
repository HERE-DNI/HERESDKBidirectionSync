---
title: "Untitled"
slug: "sdk-for-flutter-navigate-mapdata-segmentdataloader-downloadfile"
---

<HTMLBlock>{
`
<div class="sdk-for-flutter">
<!-- downloadFile.html -->

<div id="overlay-under-drawer"></div>
<header id="title">
menu
<ol class="breadcrumbs gt-separated dark hidden-xs">
<li>/sdk-for-flutter-navigate</li>
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-segmentdataloader-class</li>
<li class="self-crumb">downloadFile abstract method</li>
</ol>
<div class="self-name">downloadFile</div>
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
<div class="main-content" data-above-sidebar="mapdata/SegmentDataLoader-class-sidebar.html" data-below-sidebar="" id="dartdoc-main-content">
<div>
<h1>downloadFile abstract method</h1></div>
<section class="multi-line-signature">
List&lt;<wbr/>Uint8List&gt;
downloadFile(<wbr/><ol class="parameter-list single-line"> <li>List&lt;<wbr/>/sdk-for-flutter-navigate-mapdata-filereference-class&gt; fileReferences, </li>
<li>/sdk-for-flutter-navigate-mapdata-downloadingfileoptions-class downloadingOptions</li>
</ol>)

      

    </section>
<section class="desc markdown">
<p>Synchronously load the optional image providing guidance of a directed or non directed segment.</p>
<ul>
<li>
<p><code>fileReferences</code> Provides information for a file reference.</p>
</li>
<li>
<p><code>downloadingOptions</code> Provides information regarding downloading configuration.</p>
</li>
</ul>
<p>Returns <code>List&lt;Uint8List&gt;</code>. Requested data of a segment.</p>
<p>Throws /sdk-for-flutter-navigate-mapdata-mapdataloaderexceptionexception-class. Specifies reason, why list of data of a segment is not returned.</p>
</section>
<section class="summary source-code" id="source">
<h2>Implementation</h2>
<pre class="language-dart"><code class="language-dart">List&lt;Uint8List&gt; downloadFile(List&lt;FileReference&gt; fileReferences, DownloadingFileOptions downloadingOptions);</code></pre>
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
<li>/sdk-for-flutter-navigate-mapdata-mapdata-library</li>
<li>/sdk-for-flutter-navigate-mapdata-segmentdataloader-class</li>
<li class="self-crumb">downloadFile abstract method</li>
</ol>
<h5>SegmentDataLoader class</h5>
<div id="dartdoc-sidebar-left-content"></div>
</div>
<div class="sidebar sidebar-offcanvas-right" id="dartdoc-sidebar-right">
</div>
</main>
<footer>

    here_sdk
      4.26.0
  
</footer>



</div>
`
}</HTMLBlock>

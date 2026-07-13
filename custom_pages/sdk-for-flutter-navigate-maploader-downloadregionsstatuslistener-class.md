---
title: "DownloadRegionsStatusListener class - maploader library - Dart API"
slug: "sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-class"
---

<div id="sdk-for-flutter-navigate-overlay-under-drawer">

</div>

<div id="sdk-for-flutter-navigate-dartdoc-main-content" class="main-content" data-above-sidebar="maploader/maploader-library-sidebar.html" data-below-sidebar="maploader/DownloadRegionsStatusListener-class-sidebar.html">

<div>

# <span class="kind-class">DownloadRegionsStatusListener</span> class <a href="https://dart.dev/language/class-modifiers#abstract" class="feature feature-abstract" title="This type can not be directly constructed.">abstract</a>

</div>

<div class="section desc markdown">

Abstract class to get notified on status updates when downloading map regions.

</div>

## Constructors

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-downloadregionsstatuslistener">DownloadRegionsStatusListener</a></span><span class="signature">(<span id="sdk-for-flutter-navigate-param-onDownloadRegionsCompleteLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onDownloadRegionsCompleteLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-onProgressLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onProgressLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>, </span><span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation">int</span></span>), </span><span id="sdk-for-flutter-navigate-param-onPauseLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onPauseLambda</span>(<span id="sdk-for-flutter-navigate-param" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span></span>), </span><span id="sdk-for-flutter-navigate-param-onResumeLambda" class="parameter"><span class="type-annotation">void</span> <span class="parameter-name">onResumeLambda</span>()</span>)</span>  
Abstract class to get notified on status updates when downloading map regions.

<div class="constructor-modifier features">

factory

</div>

## Properties

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-hashcode">hashCode</a></span> <span class="signature">→ int</span>  
The hash code for this object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-runtimetype">runtimeType</a></span> <span class="signature">→ Type</span>  
A representation of the runtime type of the object.

<div class="features">

<span class="feature">no setter</span><span class="feature">inherited</span>

</div>

## Methods

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-nosuchmethod">noSuchMethod</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-noSuchMethod-param-invocation" class="parameter"><span class="type-annotation">Invocation</span> <span class="parameter-name">invocation</span></span>) <span class="returntype parameter">→ dynamic</span> </span>  
Invoked when a nonexistent method or property is accessed.

<div class="features">

<span class="feature">inherited</span>

</div>

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-ondownloadregionscomplete">onDownloadRegionsComplete</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onDownloadRegionsComplete-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span>, </span><span id="sdk-for-flutter-navigate-onDownloadRegionsComplete-param-regions" class="parameter"><span class="type-annotation">List<span class="signature">\<<wbr></wbr><span class="type-parameter"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span>\></span>?</span> <span class="parameter-name">regions</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called after the download for all requested regions has been completed with success or failure.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onpause">onPause</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onPause-param-error" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-maploadererror">MapLoaderError</a>?</span> <span class="parameter-name">error</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called when download is paused.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onprogress">onProgress</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-onProgress-param-region" class="parameter"><span class="type-annotation"><a href="sdk-for-flutter-navigate-maploader-regionid-class">RegionId</a></span> <span class="parameter-name">region</span>, </span><span id="sdk-for-flutter-navigate-onProgress-param-percentage" class="parameter"><span class="type-annotation">int</span> <span class="parameter-name">percentage</span></span>) <span class="returntype parameter">→ void</span> </span>  
Called multiple times to indicate the download progress for each requested region individually.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-onresume">onResume</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ void</span> </span>  
Called when paused download is resumed.

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-tostring">toString</a></span><span class="signature">(<wbr></wbr>) <span class="returntype parameter">→ String</span> </span>  
A string representation of this object.

<div class="features">

<span class="feature">inherited</span>

</div>

## Operators

<span class="name"><a href="sdk-for-flutter-navigate-maploader-downloadregionsstatuslistener-operator_equals">operator ==</a></span><span class="signature">(<wbr></wbr><span id="sdk-for-flutter-navigate-param-other" class="parameter"><span class="type-annotation">Object</span> <span class="parameter-name">other</span></span>) <span class="returntype parameter">→ bool</span> </span>  
The equality operator.

<div class="features">

<span class="feature">inherited</span>

</div>

</div>

<!-- /.main-content --> <!--/.sidebar-offcanvas--> <span class="no-break"> here_sdk 4.26.0 </span>


---
title: "MapPolyline.Representation (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MapItemRepresentation com.here.sdk.mapview.MapPolyline.Representation → com.here.NativeBase com.here.sdk.mapview.MapItemRepresentation com.here.sdk.mapview.MapPolyline.Representation → com.here.sdk.mapview.MapItemRepresentation com.here.sdk.mapview.MapPolyline.Representation → com.here.sdk.mapview.MapPolyline.Representation

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

Direct Known Subclasses:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashimagerepresentation" title="class in com.here.sdk.mapview">`MapPolyline.DashImageRepresentation`</a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-dashrepresentation" title="class in com.here.sdk.mapview">`MapPolyline.DashRepresentation`</a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidmulticolorrepresentation" title="class in com.here.sdk.mapview">`MapPolyline.SolidMultiColorRepresentation`</a>, <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-solidrepresentation" title="class in com.here.sdk.mapview">`MapPolyline.SolidRepresentation`</a>

<!-- -->

Enclosing class:  
<a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline" title="class in com.here.sdk.mapview">MapPolyline</a>

<div class="type-signature">

<span class="modifiers">public static class </span><span class="element-name type-name-label">MapPolyline.Representation</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-sdk-mapview-mapitemrepresentation" title="class in com.here.sdk.mapview">MapItemRepresentation</a></span>

</div>

<div class="block">

Base class to represent the visual appearance of a MapPolyline .

</div>

</div>

- <div id="sdk-for-android-navigate-nested-class-summary" class="section nested-class-summary">

  <div class="caption">

  Nested Classes

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Class

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `static enum `

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationerrorcode" class="type-name-link" title="enum class in com.here.sdk.mapview"><code>MapPolyline.Representation.InstantiationErrorCode</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Describes a reason for failing to create a MapPolyline.Representation .

  </div>

  </div>

  <div class="col-first odd-row-color">

  `static final class `

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-mapview-mappolyline-representation-instantiationexception" class="type-name-link" title="class in com.here.sdk.mapview"><code>MapPolyline.Representation.InstantiationException</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Thrown when a problem occurs while trying to create MapPolyline.Representation .

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


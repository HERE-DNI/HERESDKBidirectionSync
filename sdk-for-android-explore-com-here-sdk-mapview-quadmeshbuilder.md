---
title: "QuadMeshBuilder (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-quadmeshbuilder"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-explore-com-here-sdk-mapview-package-summary">com.here.sdk.mapview</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.mapview.MeshBuilder com.here.sdk.mapview.QuadMeshBuilder → com.here.NativeBase com.here.sdk.mapview.MeshBuilder com.here.sdk.mapview.QuadMeshBuilder → com.here.sdk.mapview.MeshBuilder com.here.sdk.mapview.QuadMeshBuilder → com.here.sdk.mapview.QuadMeshBuilder

</div>

<div id="sdk-for-android-explore-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">QuadMeshBuilder</span> <span class="extends-implements">extends <a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span>

</div>

<div class="block">

Builder for a single quad.

</div>

</div>

- <div id="sdk-for-android-explore-method-summary" class="section method-summary">

  <div id="sdk-for-android-explore-method-summary-table">

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Method

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">`MeshBuilder`</a>

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      withTextureCoordinates ( Anchor2D a, Anchor2D b, Anchor2D c, Anchor2D d)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Adds texture coordinates to a quad.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class com.here.sdk.mapview.<a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a>

  <a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#build(">`build`</a>), <a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D">`quad`</a>), <a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#triangle(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D">`triangle`</a>)

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-explore-method-detail" class="section method-details">

  - <div id="sdk-for-android-explore-withTextureCoordinates-com-here-sdk-core-Anchor2D-com-here-sdk-core-Anchor2D-com-here-sdk-core-Anchor2D-com-here-sdk-core-Anchor2D" class="section detail">

    ### withTextureCoordinates

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">MeshBuilder</a></span> <span class="element-name">withTextureCoordinates</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-explore-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> a, @NonNull <a href="sdk-for-android-explore-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> b, @NonNull <a href="sdk-for-android-explore-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> c, @NonNull <a href="sdk-for-android-explore-com-here-sdk-core-anchor2d" title="class in com.here.sdk.core">Anchor2D</a> d)</span>

    </div>

    <div class="block">

    Adds texture coordinates to a quad. Coordinates are specified as \<u,v\> with \<0,0\> representing the bottom-left and \<1,1\> upper-right corner.

    </div>

    Parameters:  
    `a` -

    Texture coordinate for vertex a. See [](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

        MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)

    </a>

    </p>

    `b` -

    Texture coordinate for vertex b. See [](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

        MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)

    </a>

    </p>

    `c` -

    Texture coordinate for vertex c. See [](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

        MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)

    </a>

    </p>

    `d` -

    Texture coordinate for vertex d. See [](sdk-for-android-explore-com-here-sdk-mapview-meshbuilder#quad(com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D,com.here.sdk.core.Point3D))

        MeshBuilder.quad(com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D, com.here.sdk.core.Point3D)

    </a>

    </p>

    Returns:  
    A <a href="sdk-for-android-explore-com-here-sdk-mapview-meshbuilder" title="class in com.here.sdk.mapview">`MeshBuilder`</a> instance.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


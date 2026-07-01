---
title: "MapMarkerCluster.CounterStyle (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.sdk.mapview.MapMarkerCluster.CounterStyle

</div>

<div id="class-description" class="section class-description">

Enclosing class:  
[MapMarkerCluster](sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster "class in com.here.sdk.mapview")

<div class="type-signature">

<span class="modifiers">public static final class
</span><span class="element-name type-name-label">MapMarkerCluster.CounterStyle</span>
<span class="extends-implements">extends <a
href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Styling options for a marker cluster which is represented by the marker
count as a text.

</div>

</div>

<div class="section summary">

- <div id="field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <table>
  <colgroup>
  <col style="width: 33%" />
  <col style="width: 33%" />
  <col style="width: 33%" />
  </colgroup>
  <thead>
  <tr>
  <th>Modifier and Type</th>
  <th>Field</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
  class="external-link"
  title="class or interface in java.lang"><code>String</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle#aboveMaxText"
  class="member-name-link"><code>aboveMaxText</code></a></td>
  <td><div class="block">
  String to display if there are more markers clustered than
  maxCountNumber .
  </div></td>
  </tr>
  <tr>
  <td><code>double</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle#fontSize"
  class="member-name-link"><code>fontSize</code></a></td>
  <td><div class="block">
  Font size of counter.
  </div></td>
  </tr>
  <tr>
  <td><code>int</code></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle#maxCountNumber"
  class="member-name-link"><code>maxCountNumber</code></a></td>
  <td><div class="block">
  Maximal number of markers represented as exact number.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-anchor2d"
  title="class in com.here.sdk.core"><code>Anchor2D</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle#textAnchor"
  class="member-name-link"><code>textAnchor</code></a></td>
  <td><div class="block">
  Anchor of counter in regards to marker cluster image.
  </div></td>
  </tr>
  <tr>
  <td><a href="sdk-for-android-explore-com-here-sdk-core-color"
  title="class in com.here.sdk.core"><code>Color</code></a></td>
  <td><a
  href="sdk-for-android-explore-com-here-sdk-mapview-mapmarkercluster-counterstyle#textColor"
  class="member-name-link"><code>textColor</code></a></td>
  <td><div class="block">
  Font color of counter.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <table>
  <colgroup>
  <col style="width: 50%" />
  <col style="width: 50%" />
  </colgroup>
  <thead>
  <tr>
  <th>Constructor</th>
  <th>Description</th>
  </tr>
  </thead>
  <tbody>
  <tr>
  <td><pre><code>CounterStyle()</code></pre></td>
  <td><div class="block">
  Creates a new instance.
  </div></td>
  </tr>
  </tbody>
  </table>

  </div>

- <div id="method-summary" class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>`, `<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="field-detail" class="section field-details">

  - <div id="textColor" class="section detail">

    ### textColor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Color](sdk-for-android-explore-com-here-sdk-core-color "class in com.here.sdk.core")</span> <span class="element-name">textColor</span>

    </div>

    <div class="block">

    Font color of counter. Default value is white.

    </div>

    </div>

  - <div id="fontSize" class="section detail">

    ### fontSize

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">double</span> <span class="element-name">fontSize</span>

    </div>

    <div class="block">

    Font size of counter. Default value is 20.

    </div>

    </div>

  - <div id="textAnchor" class="section detail">

    ### textAnchor

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type">[Anchor2D](sdk-for-android-explore-com-here-sdk-core-anchor2d "class in com.here.sdk.core")</span> <span class="element-name">textAnchor</span>

    </div>

    <div class="block">

    Anchor of counter in regards to marker cluster image. Default is at
    the center.

    </div>

    </div>

  - <div id="maxCountNumber" class="section detail">

    ### maxCountNumber

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">int</span> <span class="element-name">maxCountNumber</span>

    </div>

    <div class="block">

    Maximal number of markers represented as exact number. Values
    smaller than 2 will be clamped to 2. Default value is 99. When this
    value is changed, it is recommended to adapt aboveMaxText
    accordingly.

    </div>

    </div>

  - <div id="aboveMaxText" class="section detail">

    ### aboveMaxText

    <div class="member-signature">

    <span class="annotations">@NonNull
    </span><span class="modifiers">public</span> <span class="return-type"><a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a></span> <span class="element-name">aboveMaxText</span>

    </div>

    <div class="block">

    String to display if there are more markers clustered than
    maxCountNumber . Default value is "+99".

    </div>

    </div>

  </div>

- <div id="constructor-detail" class="section constructor-details">

  - <div id="<init>()" class="section detail">

    ### CounterStyle

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">CounterStyle</span>()

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    </div>

  </div>

</div>


---
title: "RDSEncryptionKey (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-package-summary">com.here.sdk.trafficbroadcast</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.sdk.trafficbroadcast.RDSEncryptionKey → com.here.sdk.trafficbroadcast.RDSEncryptionKey

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">RDSEncryptionKey</span> <span class="extends-implements">extends <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a></span>

</div>

<div class="block">

Represents the RDS encryption key. Fields allocation information is described in CEN ISO/CD 14819-6.

</div>

</div>

- <div id="sdk-for-android-navigate-field-summary" class="section field-summary">

  <div class="caption">

  Fields

  </div>

  <div class="summary-table three-column-summary">

  <div class="table-header col-first">

  Modifier and Type

  </div>

  <div class="table-header col-second">

  Field

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-first even-row-color">

  `short`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#encryptionId" class="member-name-link"><code>encryptionId</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Id of encryption key within the list.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `short`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#rotateRight" class="member-name-link"><code>rotateRight</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Rotate Right used for bit manipulations as a part of encryption process.

  </div>

  </div>

  <div class="col-first even-row-color">

  `short`

  </div>

  <div class="col-second even-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#startBit" class="member-name-link"><code>startBit</code></a>

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Start Bit used for bit manipulations as a part of encryption process.

  </div>

  </div>

  <div class="col-first odd-row-color">

  `short`

  </div>

  <div class="col-second odd-row-color">

  <a href="sdk-for-android-navigate-com-here-sdk-trafficbroadcast-rdsencryptionkey#xorValue" class="member-name-link"><code>xorValue</code></a>

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  XOR Value used for bit manipulations as a part of encryption process.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-summary" class="section constructor-summary">

  <div class="caption">

  Constructors

  </div>

  <div class="summary-table two-column-summary">

  <div class="table-header col-first">

  Constructor

  </div>

  <div class="table-header col-last">

  Description

  </div>

  <div class="col-constructor-name even-row-color">

      RDSEncryptionKey (short encryptionId,
       short rotateRight,
       short startBit,
       short xorValue)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new instance.

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

<!-- -->

- <div id="sdk-for-android-navigate-field-detail" class="section field-details">

  - <div id="sdk-for-android-navigate-encryptionId" class="section detail">

    ### encryptionId

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">encryptionId</span>

    </div>

    <div class="block">

    Id of encryption key within the list.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-rotateRight" class="section detail">

    ### rotateRight

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">rotateRight</span>

    </div>

    <div class="block">

    Rotate Right used for bit manipulations as a part of encryption process.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-startBit" class="section detail">

    ### startBit

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">startBit</span>

    </div>

    <div class="block">

    Start Bit used for bit manipulations as a part of encryption process.

    </div>

    </div>

  - <div id="sdk-for-android-navigate-xorValue" class="section detail">

    ### xorValue

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">short</span> <span class="element-name">xorValue</span>

    </div>

    <div class="block">

    XOR Value used for bit manipulations as a part of encryption process.

    </div>

    </div>

  </div>

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-short-short-short-short" class="section detail">

    ### RDSEncryptionKey

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">RDSEncryptionKey</span><wbr></wbr><span class="parameters">(short encryptionId, short rotateRight, short startBit, short xorValue)</span>

    </div>

    <div class="block">

    Creates a new instance.

    </div>

    Parameters:  
    `encryptionId` -

    Id of encryption key within the list.

    `rotateRight` -

    Rotate Right used for bit manipulations as a part of encryption process.

    `startBit` -

    Start Bit used for bit manipulations as a part of encryption process.

    `xorValue` -

    XOR Value used for bit manipulations as a part of encryption process.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


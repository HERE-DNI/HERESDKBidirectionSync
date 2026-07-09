---
title: "GPXDocument (API Reference)"
slug: "sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument"
---

<!-- ======== START OF CLASS DATA ======== -->

<div class="header">

<div class="sub-title">

<span class="package-label-in-type">Package</span> <a href="sdk-for-android-navigate-com-here-sdk-navigation-package-summary">com.here.sdk.navigation</a>

</div>

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object com.here.NativeBase com.here.sdk.navigation.GPXDocument → com.here.NativeBase com.here.sdk.navigation.GPXDocument → com.here.sdk.navigation.GPXDocument

</div>

<div id="sdk-for-android-navigate-class-description" class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class </span><span class="element-name type-name-label">GPXDocument</span> <span class="extends-implements">extends <a href="sdk-for-android-navigate-com-here-nativebase" title="class in com.here">NativeBase</a></span>

</div>

<div class="block">

Use the GPXDocument to load the GPX file. Only track data is used from the GPX file format (see trkType at https://www.topografix.com/GPX/1/1/#type_trkType). Any unknown elements in the file are ignored. Any known element with an invalid value returns an error. Elevation values are ignored.

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

      GPXDocument ( String gpxFilePath, GPXOptions options)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Create a GPX document from a file.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      GPXDocument ( List < GPXTrack > tracks)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Create a GPX document from a list of GPX tracks.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-navigate-method-summary" class="section method-summary">

  <div id="sdk-for-android-navigate-method-summary-table">

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

  `void`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      addTrack ( GPXTrack trackToAdd)

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Add track to GPX document.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  `static `<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation">`GPXDocument`</a>

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

      fromString ( String content, GPXOptions options)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab1 method-summary-table-tab4">

  <div class="block">

  Create a GPX document from a string.

  </div>

  </div>

  <div class="col-first even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util"><code>List</code></a>`<`<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">`GPXTrack`</a>`>`

  </div>

  <div class="col-second even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      getTracks ()

  </div>

  <div class="col-last even-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Gets the tracks stored in this GPX document.

  </div>

  </div>

  <div class="col-first odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  `boolean`

  </div>

  <div class="col-second odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

      save ( String gpxFilePath)

  </div>

  <div class="col-last odd-row-color method-summary-table method-summary-table-tab2 method-summary-table-tab4">

  <div class="block">

  Saves the document to a file.

  </div>

  </div>

  </div>

  </div>

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html" class="external-link" title="class or interface in java.lang">Object</a>

  <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()" class="external-link" title="class or interface in java.lang"><code>clone</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)" class="external-link" title="class or interface in java.lang"><code>equals</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()" class="external-link" title="class or interface in java.lang"><code>finalize</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()" class="external-link" title="class or interface in java.lang"><code>getClass</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()" class="external-link" title="class or interface in java.lang"><code>hashCode</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()" class="external-link" title="class or interface in java.lang"><code>notify</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()" class="external-link" title="class or interface in java.lang"><code>notifyAll</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()" class="external-link" title="class or interface in java.lang"><code>toString</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>, <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)" class="external-link" title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

<!-- -->

- <div id="sdk-for-android-navigate-constructor-detail" class="section constructor-details">

  - <div id="sdk-for-android-navigate-init-java-lang-String-com-here-sdk-navigation-GPXOptions" class="section detail">

    ### GPXDocument

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GPXDocument</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> gpxFilePath, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Create a GPX document from a file.

    </div>

    Parameters:  
    `gpxFilePath` -

    The path to the GPX file.

    `options` -

    The options to customize reading.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-init-java-util-List" class="section detail">

    ### GPXDocument

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">GPXDocument</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>\> tracks)</span>

    </div>

    <div class="block">

    Create a GPX document from a list of GPX tracks.

    </div>

    Parameters:  
    `tracks` -

    The list of tracks.

    </div>

  </div>

- <div id="sdk-for-android-navigate-method-detail" class="section method-details">

  - <div id="sdk-for-android-navigate-fromString-java-lang-String-com-here-sdk-navigation-GPXOptions" class="section detail">

    ### fromString

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public static</span> <span class="return-type"><a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation">GPXDocument</a></span> <span class="element-name">fromString</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> content, @NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxoptions" title="class in com.here.sdk.navigation">GPXOptions</a> options)</span> throws <span class="exceptions"><a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">InstantiationErrorException</a></span>

    </div>

    <div class="block">

    Create a GPX document from a string.

    </div>

    Parameters:  
    `content` -

    The content of a GPX file as string.

    `options` -

    The options to customize reading.

    Returns:  
    An <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxdocument" title="class in com.here.sdk.navigation">`GPXDocument`</a> instance.

    Throws:  
    <a href="sdk-for-android-navigate-com-here-sdk-core-errors-instantiationerrorexception" title="class in com.here.sdk.core.errors">`InstantiationErrorException`</a> -

    Indicates what went wrong when the instantiation was attempted.

    </div>

  - <div id="sdk-for-android-navigate-save-java-lang-String" class="section detail">

    ### save

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">boolean</span> <span class="element-name">save</span><wbr></wbr><span class="parameters">(@NonNull <a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html" class="external-link" title="class or interface in java.lang">String</a> gpxFilePath)</span>

    </div>

    <div class="block">

    Saves the document to a file. For saving the getTracks() modification before writing to a file, use GPXTrackWriter .

    </div>

    Parameters:  
    `gpxFilePath` -

    The file path where the GPX document will be saved.

    Returns:  
    `True` if the document has been saved successfully. `False` if an error has been happened during saving.

    </div>

  - <div id="sdk-for-android-navigate-addTrack-com-here-sdk-navigation-GPXTrack" class="section detail">

    ### addTrack

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="return-type">void</span> <span class="element-name">addTrack</span><wbr></wbr><span class="parameters">(@NonNull <a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a> trackToAdd)</span>

    </div>

    <div class="block">

    Add track to GPX document.

    </div>

    Parameters:  
    `trackToAdd` -

    track to add to GPX document

    </div>

  - <div id="sdk-for-android-navigate-getTracks" class="section detail">

    ### getTracks

    <div class="member-signature">

    <span class="annotations">@NonNull </span><span class="modifiers">public</span> <span class="return-type"><a href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/List.html" class="external-link" title="class or interface in java.util">List</a>\<<a href="sdk-for-android-navigate-com-here-sdk-navigation-gpxtrack" title="class in com.here.sdk.navigation">GPXTrack</a>\></span> <span class="element-name">getTracks</span>()

    </div>

    <div class="block">

    Gets the tracks stored in this GPX document.

    </div>

    Returns:  
    The tracks stored in this GPX document.

    </div>

  </div>

<!-- ========= END OF CLASS DATA ========= -->


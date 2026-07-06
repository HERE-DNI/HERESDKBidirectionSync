---
title: "MapImage (API Reference)"
slug: "sdk-for-android-explore-com-here-sdk-mapview-mapimage"
---

<div class="sub-title">

<span class="package-label-in-type">Package</span> [com.here.sdk.mapview](sdk-for-android-explore-com-here-sdk-mapview-package-summary)

</div>

<div class="inheritance" title="Inheritance Tree">

java.lang.Object → com.here.NativeBasecom.here.sdk.mapview.MapImage →
com.here.NativeBase → com.here.sdk.mapview.MapImage

</div>

<div id="sdk-for-android-explore-class-description"
class="section class-description">

<div class="type-signature">

<span class="modifiers">public final class
</span><span class="element-name type-name-label">MapImage</span>
<span class="extends-implements">extends
[NativeBase](sdk-for-android-explore-com-here-nativebase "class in com.here")</span>

</div>

<div class="block">

Represents a drawable resource that can be used by a MapMarker ,
MapMarker3D or MapImageOverlay to be shown on the map. Supported formats
are listed in ImageFormat . SVG format allows custom fonts in text using
font-family attribute by prior registration via
AssetsManager.registerFont . It is recommended to associate a resource
with a single MapImage instance in order to enable resource sharing and
reduce the amount of needed memory.

</div>

</div>

<div class="section summary">

- <div id="sdk-for-android-explore-constructor-summary"
  class="section constructor-summary">

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

      MapImage(byte[] pixelData,
       ImageFormat imageFormat)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new map image from the provided image data.

  </div>

  </div>

  <div class="col-constructor-name odd-row-color">

      MapImage(byte[] imageData,
       ImageFormat imageFormat,
       long width,
       long height)

  </div>

  <div class="col-last odd-row-color">

  <div class="block">

  Creates a new map image from the provided image data.

  </div>

  </div>

  <div class="col-constructor-name even-row-color">

      MapImage(String filePath,
       long width,
       long height)

  </div>

  <div class="col-last even-row-color">

  <div class="block">

  Creates a new map image from the provided path to the SVG Tiny or PNG
  image.

  </div>

  </div>

  </div>

  </div>

- <div id="sdk-for-android-explore-method-summary"
  class="section method-summary">

  <div class="inherited-list">

  ### Methods inherited from class java.lang.<a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html"
  class="external-link" title="class or interface in java.lang">Object</a>

  <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone()"
  class="external-link"
  title="class or interface in java.lang"><code>clone</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals(java.lang.Object)"
  class="external-link"
  title="class or interface in java.lang"><code>equals</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize()"
  class="external-link"
  title="class or interface in java.lang"><code>finalize</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass()"
  class="external-link"
  title="class or interface in java.lang"><code>getClass</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode()"
  class="external-link"
  title="class or interface in java.lang"><code>hashCode</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify()"
  class="external-link"
  title="class or interface in java.lang"><code>notify</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll()"
  class="external-link"
  title="class or interface in java.lang"><code>notifyAll</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString()"
  class="external-link"
  title="class or interface in java.lang"><code>toString</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait()"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>, <a
  href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait(long,int)"
  class="external-link"
  title="class or interface in java.lang"><code>wait</code></a>

  </div>

  </div>

</div>

<div class="section details">

- <div id="sdk-for-android-explore-constructor-detail"
  class="section constructor-details">

  - <div id="sdk-for-android-explore-<init>(byte[],com.here.sdk.mapview.ImageFormat)"
    class="section detail">

    ### MapImage

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapImage</span><span class="parameters">(@NonNull
    byte\[\] pixelData, @NonNull
    [ImageFormat](sdk-for-android-explore-com-here-sdk-mapview-imageformat "enum class in com.here.sdk.mapview") imageFormat)</span>

    </div>

    <div class="block">

    Creates a new map image from the provided image data. Currently only
    ImageFormat.PNG is accepted.

    </div>

    Parameters:  
    `pixelData` -

    Data to be used for the image. The bytes of a PNG image datastream
    are expected as defined in https://www.w3.org/TR/PNG

    `imageFormat` -

    The format of the image data to be used.

    </div>

  - <div id="sdk-for-android-explore-<init>(byte[],com.here.sdk.mapview.ImageFormat,long,long)"
    class="section detail">

    ### MapImage

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapImage</span><span class="parameters">(@NonNull
    byte\[\] imageData, @NonNull
    [ImageFormat](sdk-for-android-explore-com-here-sdk-mapview-imageformat "enum class in com.here.sdk.mapview") imageFormat,
    long width, long height)</span>

    </div>

    <div class="block">

    Creates a new map image from the provided image data.

    </div>

    Parameters:  
    `imageData` -

    Data to be used for the image. For image format
    [`ImageFormat.SVG`](sdk-for-android-explore-com-here-sdk-mapview-imageformat#SVG)
    the bytes of a UTF-8 encoded string in SVG Tiny format are expected.
    For the format specification see https://www.w3.org/TR/SVGTiny12

    `imageFormat` -

    The format of the image data to be used.

    `width` -

    The width of the image in pixels.

    `height` -

    The height of the image in pixels.

    </div>

  - <div id="sdk-for-android-explore-<init>(java.lang.String,long,long)"
    class="section detail">

    ### MapImage

    <div class="member-signature">

    <span class="modifiers">public</span> <span class="element-name">MapImage</span><span class="parameters">(@NonNull
    <a
    href="https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html"
    class="external-link" title="class or interface in java.lang">String</a> filePath,
    long width, long height)</span> throws
    <span class="exceptions">[InstantiationErrorException](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")</span>

    </div>

    <div class="block">

    Creates a new map image from the provided path to the SVG Tiny or
    PNG image. Will throw an error if either the height or width equals
    zero or the path is empty. Trying to load a file that is not
    compliant with SVG Tiny or PNG results in an undefined behavior. In
    particular, loading SVG that exceeds Tiny SVG specification may
    result in an image that exhibits unexpected artifacts. The caller
    must ensure that the file remains accessible for the entire duration
    of its usage by the SDK. If that cannot be ensured, then it is
    recommended to either copy the file to a location that remains
    accessible for the entire duration of its usage by the SDK or load
    and pass the file content to one of the MapImage constructors that
    creates instances out of image data ( MapImage(byte\[\],
    ImageFormat) , MapImage(byte\[\], ImageFormat, long, long) ).} This
    constructor needs read storage permission to be granted.

    </div>

    Parameters:  
    `filePath` -

    The path to image file.

    `width` -

    The width of image in pixels.

    `height` -

    The height of image in pixels.

    Throws:  
    [`InstantiationErrorException`](sdk-for-android-explore-com-here-sdk-core-errors-instantiationerrorexception "class in com.here.sdk.core.errors")

    Indicates what went wrong when the instantiation was attempted.

    </div>

  </div>

</div>


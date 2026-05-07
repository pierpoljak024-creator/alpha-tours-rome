# Check where the Google Share URL redirects to
$url = "https://share.google/nLOA4r6tI2EkfuttA"
try {
    $req = [System.Net.WebRequest]::Create($url)
    $req.AllowAutoRedirect = $false
    $resp = $req.GetResponse()
    Write-Host "Status: $($resp.StatusCode)"
    Write-Host "Location: $($resp.GetResponseHeader('Location'))"
    
    # If redirect, follow it
    if ($resp.StatusCode -eq 302 -or $resp.StatusCode -eq 301) {
        $location = $resp.GetResponseHeader('Location')
        Write-Host "`nFollowing redirect..."
        $req2 = [System.Net.WebRequest]::Create($location)
        $req2.AllowAutoRedirect = $true
        $resp2 = $req2.GetResponse()
        $reader = New-Object System.IO.StreamReader($resp2.GetResponseStream())
        $content = $reader.ReadToEnd()
        Write-Host "Final URL: $($resp2.ResponseUri.AbsoluteUri)"
        Write-Host "Content length: $($content.Length)"
        # Show first 500 chars
        if ($content.Length -gt 500) {
            Write-Host "`nFirst 500 chars:"
            Write-Host $content.Substring(0, 500)
        } else {
            Write-Host "`nFull content:"
            Write-Host $content
        }
    }
} catch {
    Write-Host "Error: $_"
}

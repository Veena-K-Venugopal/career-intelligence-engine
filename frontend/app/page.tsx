"use client";

import { useState } from "react";

export default function CareerEngine() {
  const [jobDescription, setJobDescription] = useState("");
  const [resumeText, setResumeText] = useState("");
  const [loading, setLoading] = useState(false);
  const [analysis, setAnalysis] = useState(null);


  const handleAnalyze = async () => {
    setLoading(true);
    try {
      const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          job_description: jobDescription,
          resume_text: resumeText,
        }),
      });

      const data = await response.json();
      setAnalysis(data);
    } catch (error) {
      console.error("Analysis failed:", error);
      alert("Something went wrong with the backend!");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-gray-50 p-8 text-black">
      <div className="max-w-4xl mx-auto">
        <h1 className="text-4xl font-bold text-blue-900 mb-2">
          Career Intelligence Engine
        </h1>
        <p className="text-gray-600 mb-8">
          Reveal the business pains and hidden skills behind any job.
        </p>

        <div className="grid gap-6">
          {/* Section 1: Inputs*/}
          <div className="bg-white p-6 rounded-xl shadow-sm border border-gray-200">
            <h2 className="text-xl font-semibold mb-4">Target Job & Your Resume</h2>
            <p className="text-sm text-gray-500 mb-4">Paste the details below to start the analysis.</p>

            <div className="space-y-4">

              {/* Job Description Input */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Job Description</label>
                <textarea
                  className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none h-40"
                  placeholder="Paste the job post here..."
                  value={jobDescription}
                  onChange={(e) => setJobDescription(e.target.value)}
                />
              </div>

              {/* Resume Text Input */}
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">Your Resume</label>
                <textarea
                  className="w-full p-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 outline-none h-40"
                  placeholder="Paste your resume text here..."
                  value={resumeText}
                  onChange={(e) => setResumeText(e.target.value)}
                />

                {/* The Analyze Button */}
                <button
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-4 rounded-lg transition-colors shadow-lg disabled:bg-gray-400 mt-4"
                  onClick={() => handleAnalyze()}
                  disabled={loading || !jobDescription || !resumeText}
                >
                  {loading ? "Analyzing..." : "Analyze Hidden Skills"}
                </button>
              </div>

            </div>
          </div>
        </div>
      </div>
    </main>
  );
}
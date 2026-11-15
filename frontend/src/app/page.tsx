const features = [
  {
    number: "01",
    title: "Requirement Analysis",
    description:
      "Understand business needs and convert them into clear AI agent requirements.",
  },
  {
    number: "02",
    title: "Agent Planning",
    description:
      "Create a structured plan describing the agents, tools, and workflows needed.",
  },
  {
    number: "03",
    title: "Blueprint Generation",
    description:
      "Generate validated agent blueprints that can be executed by a trusted runtime.",
  },
];

export default function Home() {
  return (
    <main className="min-h-screen bg-slate-950 text-white">
      <nav className="mx-auto flex max-w-7xl items-center justify-between px-6 py-6">
        <div className="flex items-center gap-3">
          <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-blue-600 font-bold">
            A
          </div>
          <span className="text-xl font-bold">AgentForge</span>
        </div>

        <span className="rounded-full border border-slate-700 px-4 py-2 text-sm text-slate-300">
          AI Agent Platform
        </span>
      </nav>

      <section className="mx-auto max-w-7xl px-6 pb-24 pt-20">
        <div className="max-w-3xl">
          <p className="mb-6 text-sm font-semibold uppercase tracking-widest text-blue-400">
            Build smarter business workflows
          </p>

          <h1 className="text-5xl font-bold leading-tight md:text-7xl">
            Turn your business needs into
            <span className="text-blue-400"> AI Agents.</span>
          </h1>

          <p className="mt-8 max-w-2xl text-lg leading-8 text-slate-400">
            Describe what your business needs. AgentForge analyzes your
            requirements, plans specialized AI agents, and generates
            validated blueprints ready for execution.
          </p>

          <a
            href="#workflow"
            className="mt-10 inline-block rounded-xl bg-blue-600 px-7 py-4 font-semibold transition hover:bg-blue-500"
          >
            Explore How It Works
          </a>
        </div>

        <section id="workflow" className="mt-28">
          <div className="mb-10">
            <p className="text-sm font-semibold uppercase tracking-widest text-blue-400">
              Platform capabilities
            </p>
            <h2 className="mt-3 text-3xl font-bold md:text-4xl">
              From idea to AI agent
            </h2>
            <p className="mt-4 max-w-2xl text-slate-400">
              AgentForge transforms business requirements into structured
              and validated AI agent configurations.
            </p>
          </div>

          <div className="grid gap-6 md:grid-cols-3">
            {features.map((feature) => (
              <article
                key={feature.number}
                className="rounded-2xl border border-slate-800 bg-slate-900 p-7 transition hover:border-blue-500"
              >
                <span className="text-sm font-bold text-blue-400">
                  {feature.number}
                </span>

                <h3 className="mt-6 text-xl font-semibold">
                  {feature.title}
                </h3>

                <p className="mt-4 leading-7 text-slate-400">
                  {feature.description}
                </p>
              </article>
            ))}
          </div>
        </section>

        <section className="mt-24 rounded-2xl border border-slate-800 bg-slate-900 p-8 md:p-12">
          <p className="text-sm font-semibold uppercase tracking-widest text-blue-400">
            Our engineering principle
          </p>

          <h2 className="mt-4 text-3xl font-bold">
            AI generates blueprints, not arbitrary code.
          </h2>

          <p className="mt-5 max-w-3xl leading-8 text-slate-400">
            AgentForge uses structured and validated configurations.
            A fixed, tested runtime executes these blueprints to improve
            reliability, security, and control.
          </p>
        </section>

        <footer className="mt-24 border-t border-slate-800 py-8 text-center text-sm text-slate-500">
          AgentForge © 2026. Building reliable AI agents for businesses.
        </footer>
      </section>
    </main>
  );
}